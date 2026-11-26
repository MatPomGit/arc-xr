"""Engineering-only paired accuracy evaluator for MSC-AR-P04."""
from dataclasses import dataclass
from collections import defaultdict
from random import Random
from statistics import mean

@dataclass(frozen=True)
class Trial:
    scene: str
    prompt: str
    target: str
    rgb: str | None
    rgb3d: str | None

def scene_differences(trials):
    groups = defaultdict(list)
    seen = set()
    for t in trials:
        if not all(isinstance(v, str) and v.strip() for v in (t.scene, t.prompt, t.target)):
            raise ValueError('Missing scene, prompt or target')
        key = (t.scene, t.prompt)
        if key in seen:
            raise ValueError('Duplicate paired trial')
        seen.add(key)
        # None is explicit abstention; missing execution must be handled upstream.
        groups[t.scene].append(int(t.rgb3d == t.target) - int(t.rgb == t.target))
    if not groups:
        raise ValueError('Empty benchmark')
    return {scene: mean(groups[scene]) for scene in sorted(groups)}

def estimate(trials, *, seed=42, replicates=10000):
    """Equal-scene weighted accuracy difference; percentile cluster bootstrap."""
    if type(replicates) is not int or replicates < 100:
        raise ValueError('At least 100 bootstrap replicates required')
    values = list(scene_differences(trials).values())
    if len(values) < 2:
        raise ValueError('At least two independent scenes required')
    rng = Random(seed)
    n = len(values)
    draws = sorted(mean(rng.choices(values, k=n)) for _ in range(replicates))
    return {'scenes': n, 'difference': mean(values), 'ci95_percentile': [draws[int(.025*(replicates-1))], draws[int(.975*(replicates-1))]], 'seed': seed, 'replicates': replicates}
