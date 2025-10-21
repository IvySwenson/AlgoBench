(async function () {
    // 当你从 /frontend/index.html 打开时，数据文件在 ../data/results.json
    const resp = await fetch('../data/results.json');
    if (!resp.ok) {
      console.error('Failed to load results.json');
      return;
    }
    const data = await resp.json(); // { AlgoName: { "100": ms, "1000": ms, ... }, ... }
  
    // 统一 x 轴（输入规模），按数值排序
    const sizes = [...new Set(
      Object.values(data).flatMap(obj => Object.keys(obj))
    )].map(Number).sort((a,b)=>a-b);
  
    // 生成 Chart.js datasets
    const palette = (i)=> `hsl(${(i*97)%360} 70% 60%)`;
    const datasets = Object.entries(data).map(([algo, series], i) => ({
      label: algo,
      data: sizes.map(n => Number(series[n] ?? series[String(n)] ?? null)),
      borderColor: palette(i),
      backgroundColor: 'transparent',
      borderWidth: 2,
      spanGaps: true,
      tension: 0.2,
      pointRadius: 2.5,
    }));
  
    // 画图
    const ctx = document.getElementById('runtimeChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: sizes.map(String),
        datasets
      },
      options: {
        responsive: true,
        scales: {
          x: { title: { display: true, text: 'Input Size (n)' } },
          y: { title: { display: true, text: 'Runtime (ms)' }, beginAtZero: true }
        },
        plugins: {
          legend: { position: 'bottom' },
          tooltip: { mode: 'nearest', intersect: false }
        }
      }
    });
  
    // 表格
    const thead = document.getElementById('thead-row');
    thead.innerHTML = ['Algorithm', ...sizes.map(String)]
      .map(h => `<th>${h}</th>`).join('');
    const tbody = document.getElementById('tbody');
    tbody.innerHTML = Object.entries(data).map(([algo, series]) => {
      const tds = sizes.map(n => {
        const val = series[n] ?? series[String(n)];
        return `<td>${val != null ? Number(val).toFixed(2) : '-'}</td>`;
      }).join('');
      return `<tr><td><b>${algo}</b></td>${tds}</tr>`;
    }).join('');
  })();
  