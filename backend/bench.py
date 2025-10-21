import argparse, json, random, statistics, time
from algos import ALGORITHMS

def make_data(n, seed):
    rnd = random.Random(seed)
    return [rnd.randrange(0, 1_000_000) for _ in range(n)]

def time_once(fn, arr):
    a = arr[:]  # 拷贝，避免原地排序影响下一次
    t1 = time.perf_counter()
    fn(a)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0  # ms

def bench(fn, n, trials, seed):
    samples = []
    for i in range(trials):
        arr = make_data(n, seed + i)
        samples.append(time_once(fn, arr))
    return statistics.median(samples)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="*", type=int, default=[100, 1000, 5000, 10000])
    parser.add_argument("--trials", type=int, default=5)
    parser.add_argument("--out", type=str, default="../data/results.json")
    args = parser.parse_args()

    results = {}
    for name, fn in ALGORITHMS.items():
        row = {}
        for n in args.sizes:
            ms = bench(fn, n, args.trials, seed=42)
            row[str(n)] = round(ms, 2)
        results[name] = row

    with open(args.out, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
