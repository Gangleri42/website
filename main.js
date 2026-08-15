// Two behaviors, nothing else: boot the emulator on demand, reveal sections on scroll.

const boot = document.getElementById("boot");
if (boot) {
  boot.addEventListener("click", () => {
    const device = document.getElementById("device");
    const frame = document.createElement("iframe");
    frame.src = "https://studio.seedhammer.space/machine.html";
    frame.title = "The SeedHammer II firmware, running as WebAssembly";
    frame.allow = "clipboard-write";
    device.replaceChildren(frame);
    frame.focus();
    const full = document.createElement("p");
    full.className = "microline";
    full.innerHTML = '<a href="https://studio.seedhammer.space/machine.html">Open full screen ↗</a>';
    device.after(full);
  });
}

if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const seen = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        seen.unobserve(e.target);
      }
    }
  }, { rootMargin: "0px 0px -8% 0px" });
  document.querySelectorAll(".reveal").forEach((s) => seen.observe(s));
} else {
  document.querySelectorAll(".reveal").forEach((s) => s.classList.add("in"));
}
