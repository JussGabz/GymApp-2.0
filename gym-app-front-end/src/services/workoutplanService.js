import { getToken } from "../utils/tokenUtils";
import { WORKOUT_PLANS_ENDPOINT } from "../config/apiConfig";
import Error from "../component/Error";

// Fetch Workout Plan from backend workout plan endpoint
// Isolate the API Call Logic -> Make it easy to replace or modify if api changes
export const fetchWorkoutPlans = async (searchQuery = "") => {
    const token = getToken()

    // Append search Query as a query parameter if provided

    const url = searchQuery
        ? `${WORKOUT_PLANS_ENDPOINT}?name=${encodeURIComponent(searchQuery)}`
        : WORKOUT_PLANS_ENDPOINT;
    
    try {
        const response = await fetch( url, {
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