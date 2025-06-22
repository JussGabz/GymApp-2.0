import { getToken } from "../utils/tokenUtils";
import { WORKOUT_PLANS_ENDPOINT, API_BASE_URL } from "../config/apiConfig";
import Error from "../component/Error";

// Fetch Workout Plan from backend workout plan endpoint
// Isolate the API Call Logic -> Make it easy to replace or modify if api changes
export const fetchWorkoutPlans = async (url = WORKOUT_PLANS_ENDPOINT) => {
    const token = getToken()

    // Append search Query as a query parameter if provided
    console.log(url)
    try {
        const response = await fetch( url , {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${token}`,
            }
        })

        if (!response.ok) {
            throw new Error('Failed to fetch workout plans')
        }
        return await response.json()
    } catch (error) {
        console.error()
    }
} 