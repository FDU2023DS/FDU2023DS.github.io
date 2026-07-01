---
layout: page
permalink: /calendar/
title: calendar
description: Calendar for courses, class meetings, and other events.
nav: true
nav_order: 4

---

<style>
  .fc-daygrid-day-events{
    font-size: 12px;
  }
</style>

<script src="../assets/js/index.global.min.js?v={{ 'v' | date: '%s' }}"></script>

<script>

  document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
      },
      initialDate: '2026-07-01T04:51:04+08:00',
      navLinks: true, // can click day/week names to navigate views
      businessHours: true, // display business hours
      editable: true,
      selectable: true,
      themeSystem: 'bootstrap',
      events: []
    });

    // 动态加载events
    fetch('../assets/json/calendar_events.json')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to load events JSON');
        }
        return response.json();
      })
      .then(events => {
        // 将加载的事件数据添加到日历中
        calendar.addEventSource(events);
      })
      .catch(error => {
        console.error('Error loading events:', error);
      });

    calendar.render();
  });

</script>

<div id='calendar'></div>

<style>
  .fc-daygrid-dot-event .fc-event-title {
    text-overflow: ellipsis;
  }
  .fc-icon{
    color: white;
  }
</style>
