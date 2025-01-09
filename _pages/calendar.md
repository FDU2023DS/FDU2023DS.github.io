---
layout: page
permalink: /calendar/
title: Calendar
description: Calendar for courses, class meetings, and other events.
nav: true
nav_order: 4

---

<script src='../dist/index.global.js'></script>
<div id='calendar'>
<head>
<meta charset='utf-8' />
<script src='../dist/index.global.js'></script>
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
    fetch('../dist/calendar-events.json')
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
<style>

  body {
    margin: 40px 10px;
    padding: 0;
    font-family: Arial, Helvetica Neue, Helvetica, sans-serif;
    font-size: 14px;
  }

  #calendar {
    max-width: 1100px;
    margin: 0 auto;
  }

</style>
</head>
<body>

  <div id='calendar'></div>

</body>

</div>