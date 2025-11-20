(() => {
  const listenButton = document.getElementById("btnListen");
  if (!listenButton) return;

  const PRESS_CLASS = "is-pressed";
  let releaseTimer = null;

  const startPress = () => {
    if (releaseTimer) {
      clearTimeout(releaseTimer);
      releaseTimer = null;
    }
    listenButton.classList.add(PRESS_CLASS);
  };

  const endPress = () => {
    releaseTimer = window.setTimeout(() => {
      listenButton.classList.remove(PRESS_CLASS);
      releaseTimer = null;
    }, 80);
  };

  listenButton.addEventListener(
    "pointerdown",
    () => {
      startPress();
    },
    { passive: true }
  );

  listenButton.addEventListener(
    "pointerup",
    () => {
      endPress();
    },
    { passive: true }
  );

  listenButton.addEventListener(
    "pointerleave",
    () => {
      endPress();
    },
    { passive: true }
  );

  listenButton.addEventListener(
    "pointercancel",
    () => {
      endPress();
    },
    { passive: true }
  );

  listenButton.addEventListener(
    "click",
    () => {
      startPress();
      releaseTimer = window.setTimeout(() => {
        listenButton.classList.remove(PRESS_CLASS);
        releaseTimer = null;
      }, 420);
    },
    { passive: true }
  );

  listenButton.addEventListener("animationend", (event) => {
    if (event.animationName === "listenPulse" || event.animationName === "listenRing") {
      listenButton.classList.remove(PRESS_CLASS);
    }
  });
})();
