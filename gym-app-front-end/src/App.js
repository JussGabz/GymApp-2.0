import 'bootstrap/dist/css/bootstrap.min.css';

// App.js or Routes.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Homepage from './Homepage';
import WorkoutPage from './WorkoutPage'
import ExercisePage from './ExercisePage'

const App = () => {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Homepage />} />
        <Route path="/workouts" Component={WorkoutPage} />
        <Route path="/exercises" Component={ExercisePage} />
      </Routes>
    </Router>
  );
};

export default App;
