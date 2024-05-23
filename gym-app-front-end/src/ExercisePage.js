import React, { useState, useEffect } from 'react';
import Menu from './Menu';
import Exercises from './component/exercises';

const ExercisePage = () => {
    return (
      <div>
        < Menu />
        < Exercises />
      </div>
    );
  };
  
  export default ExercisePage;