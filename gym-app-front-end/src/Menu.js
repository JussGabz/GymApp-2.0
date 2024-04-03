// Menu.js
import React from 'react';

const Menu = () => {
    return (
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container">
          <a className="navbar-brand" href="/">JussGym</a>
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <a className="nav-link" href="/workouts">Workout Plans</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/exercises">Exercises</a>
              </li>
              {/* Add more menu items as needed */}
            </ul>
          </div>
        </div>
      </nav>
    );
  };

export default Menu;