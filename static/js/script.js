const voiceInputBtn = document.getElementById("voiceInput");
const voiceIcon = document.getElementById("voiceIcon");

// Check if the browser supports Web Speech API
const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;
if (!SpeechRecognition) {
  alert("Browser Anda tidak mendukung fitur input suara.");
} else {
  const recognition = new SpeechRecognition();
  recognition.lang = "id-ID"; // Bahasa Indonesia
  recognition.interimResults = false;

  // Handle button click
  voiceInputBtn.addEventListener("click", () => {
    if (voiceInputBtn.classList.contains("active")) {
      recognition.stop();
      voiceInputBtn.classList.remove("active");
      voiceIcon.classList.replace("fa-stop", "fa-microphone");
    } else {
      recognition.start();
      voiceInputBtn.classList.add("active");
      voiceIcon.classList.replace("fa-microphone", "fa-stop");
    }
  });

  // On recognition result
  recognition.addEventListener("result", (event) => {
    const speechToText = event.results[0][0].transcript;

    // Kirim pesan langsung tanpa memasukkan ke input box
    appendMessage("You", "static/images/person.svg", "right", speechToText);
    botResponse(speechToText);

    // Reset tombol ke kondisi awal
    voiceInputBtn.classList.remove("active");
    voiceIcon.classList.replace("fa-stop", "fa-microphone");
  });

  // Handle recognition end
  recognition.addEventListener("end", () => {
    voiceInputBtn.classList.remove("active");
    voiceIcon.classList.replace("fa-stop", "fa-microphone");
  });

  // Handle errors
  recognition.addEventListener("error", (event) => {
    console.error("Recognition Error:", event.error);
    alert("Terjadi kesalahan saat menggunakan input suara.");
  });
}
