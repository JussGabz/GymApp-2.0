import { useEffect, useState } from "react"
import { WORKOUT_PLANS_ENDPOINT } from "../../config/apiConfig"
import { fetchWorkoutPlans } from "../../services/workoutplanService"

function WorkoutPlanDropdown() {
    const [workoutPlans, setWorkoutPlans] = useState([])
    const [selected, setSelected] = useState([])
    const [url, setCurrentUrl] = useState(WORKOUT_PLANS_ENDPOINT)

    useEffect(() => {
        fetchWorkoutPlan(url)
    }, [url])

    const fetchWorkoutPlan = async (url) => {
        try {
            
        }
    }
}