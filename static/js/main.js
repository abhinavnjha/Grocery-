document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".flash").forEach(function (el, i) {
    setTimeout(function () {
      el.style.transition = "opacity .4s";
      el.style.opacity = "0";
      setTimeout(function () { el.remove(); }, 400);
    }, 3000 + i * 300);
  });
});
