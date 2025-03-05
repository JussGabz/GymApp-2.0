// Menu.js
import React from 'react';
import './css/Menu.css'

const Menu = () => {
  return (
    <nav className="menu">
      <div className="logo">Juss Gym</div>
      <ul className="menu-links">
        <li className="menu-item"><a href="/exercises">Exercises</a></li>
        <li className="menu-item"><a href="/workouts">Workout Plans</a></li>
        <li className="menu-item"><a href="/login">Login</a></li>
      </ul>
    </nav>
  );
};

export default Menu;
