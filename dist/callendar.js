document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
    },
    initialDate: '2025-02-17',
    navLinks: true, // can click day/week names to navigate views
    businessHours: true, // display business hours
    editable: true,
    selectable: true,
    events: []
  });

  fetch('dist/calendar-events.json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to load events JSON');
      }
      return response.json();
    })
    .then(events => {
      calendar.addEventSource(events);
    })
    .catch(error => {
      console.error('Error loading events:', error);
    });

  calendar.render();
});