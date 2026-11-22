// The browser side. HTML alone can't react to clicks, so a little JavaScript
// is unavoidable. Keep it small: fetch data from your Python API, draw squares,
// react to taps. All the real logic belongs in Python.

// TODO 4.3: function loadDays()
//   fetch("/api/days"), then draw one square per day into #grid.
//   Each square needs to remember which day number it is (look up data- attributes).

// TODO 5.2: left click / tap on a square -> open the details panel for that day
//   fetch(`/api/days/${n}`) and fill the panel.

// TODO 5.3: right click on a square -> toggle complete
//   Look up the "contextmenu" event and event.preventDefault().
//
//   ⚠ THINK BEFORE YOU CODE THIS ONE: your phone has no right mouse button.
//   What does a long-press do on Android Chrome? On iPhone Safari?
//   Test it on your actual phone. You may need a second way to mark a
//   day complete (a button inside the details panel?).

// TODO 5.4: the "log a session" form inside the panel
//   POST to /api/sessions, then refresh the panel AND the grid. Why both?

// loadDays();   // <- uncomment once TODO 4.3 exists
