# Как будут выглядеть ударения в HTML

<!-- Copy-paste -->
<style>
  .jp-sample {
    font-family: "Hiragino Mincho ProN", "Yu Mincho", "Noto Serif JP", "Noto Sans JP", sans-serif;
    font-size: 28px;
    line-height: 1.55;
  }
  .jp-line { margin: 4px 0; }
  .ol {
    text-decoration: overline;
    text-decoration-thickness: 2px;
    text-decoration-skip-ink: none;
  }
</style>

<div class="jp-sample" lang="ja" id="jpAccentBlock">
  <!-- ✅ Как ставить линии:
       Пиши: ま[どぐ]ち  → линия будет над "どぐ"
       Можно несколько раз в слове: こ[い]び[と] и т.п.
  -->

  <div class="jp-line">ま[ど]ぐち、[か]ざん、こ[づ]つみ、[は]なび、あ[まぐ]も、こ[いびと]</div>
  <div class="jp-line">こ[とばづ]かい、は[いざら]、い[け]ばな、し[たぎ]、あ[おじろ]い、[で]ぐち</div>
  <div class="jp-line">わ[りびき]、りょ[うがえ]、あ[っぱく]、じ[っし]、け[っかん]、は[ってん]</div>
</div>

<script>
  // Converts [...] to <span class="ol">...</span>
  (function applyOverlines(rootId) {
    const root = document.getElementById(rootId);
    if (!root) return;

    const escapeHtml = (s) =>
      s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

    for (const line of root.querySelectorAll(".jp-line")) {
      const raw = line.textContent;
      // Replace [xxx] with overline span
      const html = escapeHtml(raw).replace(/\[([^\]]+)\]/g, '<span class="ol">$1</span>');
      line.innerHTML = html;
    }
  })("jpAccentBlock");
</script>