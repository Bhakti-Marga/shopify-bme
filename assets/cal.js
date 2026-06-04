document.addEventListener("DOMContentLoaded", function () {
  var calendarEl = document.getElementById("calendar");

  var colorMap = {
    "Localizacion Málaga":                    "#E57373",
    "Localizacion Comunidad Turzás - Galicia":"#81C784",
    "Localizacion Vizcaya":                   "#64B5F6",
    "Localizacion Barcelona":                 "#FFB74D",
    "Localizacion Guipuzcoa":                 "#BA68C8",
    "Localizacion Riba roja Valencia":        "#4DB6AC",
    "Localizacion Canals Valencia":           "#F06292",
    "Localizacion Lanzarote":                 "#FFD54F",
    "Localización Madrid":                    "#A1887F"
  };

  function mobileCheck() {
    return !(window.innerWidth >= 768);
  }

  var events = (window.shopifyEvents || []).map(function(e) {
    return {
      title: e.title,
      start: e.start,
      end: e.end || null,
      url: e.url,
      backgroundColor: colorMap[e.location] || "#90A4AE",
      borderColor: colorMap[e.location] || "#90A4AE"
    };
  });

  var calendar = new FullCalendar.Calendar(calendarEl, {
    timeZone: "Europe/Madrid",
    themeSystem: "bootstrap5",
    headerToolbar: {
      left: mobileCheck() ? "prev" : "prev,next today",
      center: "title",
      right: mobileCheck() ? "next" : "dayGridMonth,timeGridWeek,timeGridDay,listMonth"
    },
    weekNumbers: false,
    firstDay: 1,
    initialView: mobileCheck() ? "listMonth" : "dayGridMonth",
    defaultAllDay: true,
    dayMaxEvents: false,
    events: events
  });

  calendar.render();
});
