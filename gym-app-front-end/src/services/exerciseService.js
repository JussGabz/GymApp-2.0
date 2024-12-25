import { getToken } from "../utils/tokenUtils";
import { EXERCISES_ENDPOINT } from "../config/apiConfig";

// Fetch Exercises from backend exercise endpoint
// Isolate the API Call Logic -> Make it easy to replace or modify if API changes
export const fetchExercises = async () => {
    const token = getToken()
    const response = await fetch( EXERCISES_ENDPOINT, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
        }
    })
    if (!response.ok) {
        throw new Error('Failed to fetch exercises')
    }
    return await response.json()
}