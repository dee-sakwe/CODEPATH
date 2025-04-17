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

// Step 1: Add your query for the submit RSVP button here
const rsvpForm = document.getElementById("rsvp-form");

let rsvpCount = 3;

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

function addParticipant() {

    const fullName = document.getElementById("name").value;
    const firstName = fullName.trim().split(" ")[0];
    const hometownInput = document.getElementById("hometown").value;

    const newParticipant = document.createElement("p");
    newParticipant.textContent = `🍛 ${firstName} from ${hometownInput} has RSVP'd.`;
    newParticipant.classList.add("participant-entry");

    const participantsDiv = document.querySelector(".rsvp-participants");
    participantsDiv.appendChild(newParticipant);

    const countElement = document.getElementById("rsvp-count");
    if (countElement) countElement.remove();

    rsvpCount += 1;

    const newCountElement = document.createElement("p");
    newCountElement.id = "rsvp-count";
    newCountElement.innerHTML = `<span id="rsvp-number"><strong>0</strong></span> people have RSVP'd to this event.`;
    newCountElement.classList.add("slide-up");
    participantsDiv.appendChild(newCountElement);

    animateNumber("rsvp-number", rsvpCount - 1, rsvpCount, 800);

    confetti({
        particleCount: 75,
        spread: 75,
        origin: { y: 0.6 },
    });

    rsvpForm.reset();

    const successMsg = document.getElementById("rsvp-success");
    successMsg.style.display = "block";

    setTimeout(() => {
        successMsg.style.display = "none";
    }, 5000);
}

// Step 3: Add a click event listener to the submit RSVP button here
// rsvpForm.addEventListener("submit", addParticipant);

/*** Form Validation ***
  
  Purpose:
  - Prevents invalid form submissions from being added to the list of participants.

  When To Modify:
  - [ ] Project 7 (REQUIRED FEATURE)
  - [ ] Project 7 (STRETCH FEATURE)
  - [ ] Project 9 (REQUIRED FEATURE)
  - [ ] Any time between / after
***/

// Step 1: We actually don't need to select the form button again -- we already did it in the RSVP code above.

// Step 2: Write the callback function
const validateForm = (event) => {
    event.preventDefault(); // stop the real submit
  
    let containsErrors = false;
    const allControls = document.getElementById("rsvp-form").elements;
  
    // Convert to array and filter to only inputs
    const inputs = Array.from(allControls).filter(el => el.tagName === "INPUT");
  
    inputs.forEach(input => {
      if (input.value.trim().length < 2) {
        containsErrors = true;
        input.classList.add("error");
      } else {
        input.classList.remove("error");
      }
    });

    // 2) Grab the email field
    const emailInput = document.getElementById("email");
    const emailValue = emailInput.value.trim();

    // 3) If it doesn’t include “.com”, flag an error
    if (!emailValue.includes(".com")) {
        containsErrors = true;
        emailInput.classList.add("error");
    } else {
        emailInput.classList.remove("error");
    }
  
    if (!containsErrors) {
      addParticipant();         // now this will actually run
      inputs.forEach(i => i.value = "");  // clear them
    }
};
  
// Step 3: Replace the form button's event listener with a new one that calls validateForm()
rsvpForm.addEventListener("submit", validateForm);

/*** Animations [PLACEHOLDER] [ADDED IN UNIT 8] ***/
/*** Success Modal [PLACEHOLDER] [ADDED IN UNIT 9] ***/
