// HomePage.js
import React from 'react';
import Menu from './Menu';
import Exercises from './component/exercises';

const HomePage = () => {
  return (
    <div>
      < Menu />
      <h1>Juss Gym</h1>
      <h5>Workout with JussGym</h5>
      {/* Add more content as needed */}
      <video width={800} height={500} controls loop autoPlay muted>
        <source
          src='https://d164p06em7ia.cloudfront.net/C0201.MP4'
          type='video/mp4'
        />
      </video>

      <div>
      < Exercises />
      </div>
    </div>
  );
};

export default HomePage;