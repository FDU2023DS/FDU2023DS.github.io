---
layout: page
permalink: /calendar/
title: calendar
description: Calendar for courses, class meetings, and other events.
nav: true
nav_order: 4

---

<style>

  body {
    margin: 40px 10px;
    padding: 0;
    font-size: 12px;
  }

  #calendar {
    max-width: 1100px;
    margin: 0 auto;
    float: left;
  }

</style>

<script src='https://cdn.jsdelivr.net/npm/fullcalendar-scheduler@6.1.15/index.global.min.js'></script>
<script>

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
