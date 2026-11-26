"""Generate publication-oriented artifacts from a validated development matrix."""
import argparse
import hashlib
import json
from pathlib import Path
from robustness import analyze
from PIL import Image, ImageDraw

def export(root, output):
    rows=analyze(root)
    output=Path(output)
    output.mkdir(parents=True,exist_ok=False)
    # All values are numeric, never interpolate model output into TeX.
    lines=[r"\begin{tabular}{rrrrrr}",r"\hline",
           r"$\sigma$ (cm) & Mask (\%) & $n$ & RGB (\%) & RGB+3D (\%) & $\Delta$ (pp) \\",r"\hline"]
    for row in rows:
        lines.append(f'{row["sigma_cm"]} & {row["occlusion_pct"]} & {row["n_scenes"]} & {100*row["rgb_accuracy"]:.1f} & {100*row["rgb3d_accuracy"]:.1f} & {100*row["gain"]:.1f} '+r"\\")
    lines.extend([r"\hline",r"\end{tabular}"])
    (output/"robustness_table.tex").write_text("\n".join(lines)+"\n",encoding="utf-8")
    # Dependency-free SVG with fixed axes, percent-point gain and pointwise intervals.
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="760" height="500" viewBox="0 0 760 500">',
         '<rect width="760" height="500" fill="white"/>',
         '<g font-family="sans-serif" font-size="15" fill="#222">',
         '<text x="380" y="27" text-anchor="middle" font-size="19">Development pilot: geometry advantage</text>',
         '<text x="380" y="480" text-anchor="middle">Geometry noise sigma (cm)</text>',
         '<text x="18" y="230" transform="rotate(-90 18 230)" text-anchor="middle">Accuracy difference (percentage points)</text>']
    def x(s): return 100+100*s
    def y(v): return 230-180*v
    for v in (-1,-.5,0,.5,1):
        svg.append(f'<path d="M100 {y(v)} H600" stroke="#ddd"/>')
        svg.append(f'<text x="90" y="{y(v)+5}" text-anchor="end">{100*v:g}</text>')
    for s in (0,2,5):
        svg.append(f'<text x="{x(s)}" y="435" text-anchor="middle">{s}</text>')
    svg.append('<path d="M100 50 V410 H600" fill="none" stroke="#222"/>')
    for i,(o,color) in enumerate(((0,"#0072b2"),(10,"#d55e00"),(25,"#009e73"))):
        group=sorted((r for r in rows if r["occlusion_pct"]==o),key=lambda r:r["sigma_cm"])
        shift=(i-1)*7
        svg.append('<polyline fill="none" stroke="'+color+'" stroke-width="2.5" points="'+" ".join(f'{x(r["sigma_cm"])+shift},{y(r["gain"])}' for r in group)+'"/>')
        for r in group:
            xx=x(r["sigma_cm"])+shift; yy=y(r["gain"]); a=y(r["gain_lo"]); b=y(r["gain_hi"])
            svg.append(f'<path d="M{xx} {a} V{b} M{xx-4} {a} H{xx+4} M{xx-4} {b} H{xx+4}" stroke="{color}" fill="none"/>')
            svg.append(f'<circle cx="{xx}" cy="{yy}" r="4" fill="{color}"/>')
        svg.append(f'<text x="620" y="{80+i*26}" fill="{color}">Mask {o}%</text>')
    svg.append('</g></svg>')
    (output/"robustness.svg").write_text("\n".join(svg),encoding="utf-8")
    root=Path(root)
    inputs={}
    for path in sorted(root.glob("s*_o*/*")):
        if path.name in ("manifest.json","ground_truth.json","pilot.jsonl"):
            inputs[str(path.relative_to(root))]=hashlib.sha256(path.read_bytes()).hexdigest()
    (output/"report.json").write_text(json.dumps({"scope":"exploratory_development","inputs_sha256":inputs,"rows":rows},indent=2),encoding="utf-8")

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("root");p.add_argument("output")
    a=p.parse_args();export(a.root,a.output)
