import React from "react"
import WorkoutForm from "./WorkoutForm"
import { Container, Button, Card, Row, Col } from "react-bootstrap"
import ExerciseDropdown from "./SelectExercises"

function CreateWorkoutPlan() {

    return (
        <Container className="text-center mt-4">
            {/* Workout Name */}
            <p>dsdd</p>
            <p>dssdvd</p>
            <ExerciseDropdown/>
            <WorkoutTypeDropdown/>
            <WorkoutForm/>
            

        </Container>
    )
}

export default CreateWorkoutPlan