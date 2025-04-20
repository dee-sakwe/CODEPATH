/*** Dark Mode ***
  
  Purpose:
  - Use this starter code to add a dark mode feature to your website.

  When To Modify:
  - [ ] Project 5 (REQUIRED FEATURE) 
  - [ ] Any time after
***/

// Step 1: Select the theme button
let themeButton = document.getElementById("theme-button");

// Step 2: Write the callback function
const toggleDarkMode = () => {
  document.body.classList.toggle("dark-mode");

  document.documentElement.style.background = 
      document.body.classList.contains("dark-mode") 
      ? "linear-gradient(to bottom, #1a1a2e, #16213e)" 
      : "linear-gradient(to bottom, #f9f9f9, #f3eadb)";

  if (document.body.classList.contains("dark-mode")) {
      themeButton.innerHTML = "Light ☀️"; 
      themeButton.style.backgroundColor = "#231942"; 
      themeButton.style.color = "#e89c2a";

      themeButton.onmouseover = () => {
          themeButton.style.backgroundColor = "#04724D"; 
          themeButton.style.color = "white"; 
      };

      themeButton.onmouseout = () => {
          themeButton.style.backgroundColor = "#231942"; 
          themeButton.style.color = "#e89c2a"; 
      };
  } else {
      themeButton.innerHTML = "Dark 🌙"; 
      themeButton.style.backgroundColor = "#04724D"; 
      themeButton.style.color = "black";

      themeButton.onmouseover = () => {
          themeButton.style.backgroundColor = "#231942"; 
          themeButton.style.color = "white"; 
      };

      themeButton.onmouseout = () => {
          themeButton.style.backgroundColor = "#04724D"; 
          themeButton.style.color = "black"; 
      };
  }
};

// Step 3: Register a 'click' event listener for the theme button,
//             and tell it to use toggleDarkMode as its callback function
themeButton.addEventListener("click", toggleDarkMode);


/*** Form Handling ***
  
  Purpose:
  - When the user submits the RSVP form, the name and state they 
    entered should be added to the list of participants.

  When To Modify:
  - [ ] Project 6 (REQUIRED FEATURE)
  - [ ] Project 6 (STRETCH FEATURE) 
  - [ ] Project 7 (REQUIRED FEATURE)
  - [ ] Project 9 (REQUIRED FEATURE)
  - [ ] Any time between / after
***/

// Helper funtion for animating the number everytime it increases
function animateNumber(id, start, end, duration) {
    const element = document.getElementById(id);
    let startTime = null;

    function step(timestamp) {
        if (!startTime) startTime = timestamp;
        const progress = timestamp - startTime;
        const value = Math.min(Math.floor(start + (end - start) * (progress / duration)), end);
        element.innerHTML = `<strong>${value}</strong>`;

        if (value < end) {
            window.requestAnimationFrame(step);
        }
    }

    window.requestAnimationFrame(step);
}

// Step 0: grab the form once
const rsvpForm = document.getElementById("rsvp-form");
let rsvpCount = 3;

// ————————————————————————————————
// validateForm now builds a `person` object
// ————————————————————————————————
function validateForm(event) {
  event.preventDefault();

  // pull values just once
  const nameValue     = document.getElementById("name").value.trim();
  const emailValue    = document.getElementById("email").value.trim();
  const hometownValue = document.getElementById("hometown").value.trim();

  // bundle into an object
  const person = {
    name:     nameValue,
    email:    emailValue,
    hometown: hometownValue
  };

  // validation flag
  let containsErrors = false;

  // clear any old errors
  [ "name", "email", "hometown" ].forEach(field => {
    document.getElementById(field).classList.remove("error");
  });

  // validate name
  if (person.name.length < 2) {
    containsErrors = true;
    document.getElementById("name").classList.add("error");
  }

  // validate email
  if (!person.email.includes(".com")) {
    containsErrors = true;
    document.getElementById("email").classList.add("error");
  }

  // validate hometown
  if (person.hometown.length < 2) {
    containsErrors = true;
    document.getElementById("hometown").classList.add("error");
  }

  if (!containsErrors) {
    addParticipant(person);
    rsvpForm.reset();
  }
}

// 1. Grab the modal and the Close button
const modal      = document.getElementById("success-modal");
const closeBtn   = document.getElementById("modal-close");

// 2. Create a variable to hold our timeout ID
let modalTimer = null;

// 3. Show and hide helpers, with auto‐hide in showModal()
function showModal() {
  modal.classList.add("show");

  // clear out any previous timer
  clearTimeout(modalTimer);

  // set new timer: hide in 5 seconds
  modalTimer = setTimeout(hideModal, 7000);
}

function hideModal() {
  modal.classList.remove("show");

  // also clear the timer to avoid calling hideModal again
  clearTimeout(modalTimer);
}

// 4. Close when user clicks the “Close” button
closeBtn.addEventListener("click", hideModal);

modal.addEventListener("click", e => {
  // clicking outside the container closes it
  if (e.target === modal) hideModal();
});

// ————————————————————————————————
// addParticipant now takes that `person` object
// ————————————————————————————————
function addParticipant(person) {
  const participantsDiv = document.querySelector(".rsvp-participants");

  // 1) new participant line
  const newP = document.createElement("p");

  // get the raw first name
  const rawFirst = person.name.split(" ")[0];

// capitalize it
  const firstName = rawFirst.charAt(0).toUpperCase() + rawFirst.slice(1).toLowerCase();
  newP.textContent = `🍛 ${firstName} from ${person.hometown} has RSVP'd.`;
  newP.classList.add("participant-entry");
  participantsDiv.appendChild(newP);

  // 2) update count
  document.getElementById("rsvp-count")?.remove();
  rsvpCount++;
  const countP = document.createElement("p");
  countP.id = "rsvp-count";
  countP.innerHTML = `<span id="rsvp-number"><strong>0</strong></span> people have RSVP'd to this event!`;
  countP.classList.add("slide-up");
  participantsDiv.appendChild(countP);

  animateNumber("rsvp-number", rsvpCount - 1, rsvpCount, 800);

  // 3) confetti + success
  confetti({ particleCount:75, spread:75, origin:{y:0.6} });
  document.getElementById("rsvp-success").style.display = "block";
  setTimeout(()=> document.getElementById("rsvp-success").style.display = "none", 9000);

  showModal();
}

// wire it up
rsvpForm.addEventListener("submit", validateForm);

// —————————— Scroll Animation ——————————

// 1. Prepare the observer
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    // only toggle if motion is allowed
    if (!document.body.classList.contains('reduce-motion')) {
      entry.target.classList.toggle('in-view', entry.isIntersecting);
    }
  });
}, { threshold: 0.1 });

// 2. Pick your real targets
const targets = document.querySelectorAll(
  '.about-text, .about-expect, .about-content, .event-container, .rsvp-container, .links-container, .form-container, #title'
);

// 3. Hide & observe each
targets.forEach(el => {
  el.classList.add('scroll-animate');
  observer.observe(el);
});


// —————— Reduce Motion Toggle ——————

const reduceBtn = document.getElementById('reduce-motion-button');
reduceBtn.addEventListener('click', () => {
  document.body.classList.toggle('reduce-motion');

  if (document.body.classList.contains('reduce-motion')) {
    // user wants no motion: force everything into view and stop observing
    targets.forEach(el => {
      el.classList.add('in-view');
      observer.unobserve(el);
    });
  } else {
    // re‑enable motion: hide again then re‑observe
    targets.forEach(el => {
      el.classList.remove('in-view');
      observer.observe(el);
    });
  }
});
