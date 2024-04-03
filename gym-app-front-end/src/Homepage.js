// HomePage.js
import React from 'react';
import Menu from './Menu';
import WorkoutPage from './WorkoutPage'
import ExercisePage from './ExercisePage'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';


const HomePage = () => {
  return (
    <div>
      < Menu />
      <h1>Juss Gym</h1>
      <p>Workout with JussGym</p>
      {/* Add more content as needed */}
      <video width={800} height={500} controls loop autoPlay muted>
        <source
          src='https://d164p06em7ia.cloudfront.net/C0201.MP4'
          type='video/mp4'
        />
      </video>
    </div>
  );
};

export default HomePage;