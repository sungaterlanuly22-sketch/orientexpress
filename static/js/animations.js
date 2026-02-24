// === Плавное появление элементов при скролле ===
const faders = document.querySelectorAll(".fade-up");

const appearOptions = {
  threshold: 0.2
};

const appearOnScroll = new IntersectionObserver(function(entries){
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add("show");
  });
}, appearOptions);

faders.forEach(fader => {
  appearOnScroll.observe(fader);
});


// === АВТОСЛАЙДЕР ГАЛЕРЕИ ===
const slider = document.querySelector(".slider");

if (slider) {
  let scrollAmount = 0;

  setInterval(() => {
    scrollAmount += slider.clientWidth;

    if (scrollAmount >= slider.scrollWidth) {
      scrollAmount = 0;
    }

    slider.scrollTo({
      left: scrollAmount,
      behavior: "smooth"
    });
  }, 3000);
}


// === КНОПКА ЧАТ (клик) ===
const chatBtn = document.querySelector(".chat-btn");

if (chatBtn) {
  chatBtn.addEventListener("click", () => {
    alert("Чат скоро будет подключен");
  });
}