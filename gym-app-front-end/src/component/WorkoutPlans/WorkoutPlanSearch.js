import React, { useState } from "react";
import SearchBar from "../../genericSearchBar";
import { fetchWorkoutPlans } from "../../services/workoutplanService";

function WorkoutPlanSearchBar({ onSearch }) {
    const [searchQuery, setSearchQuery] = useState('')

    const handleSearchChange = (newValue) => {
        setSearchQuery(newValue)
    }

    const handleSearch = async (query) => {
        console.log(`Searching for: ${query}`)

        // const data = await fetchWorkoutPlans()
        const data = onSearch(searchQuery)

        console.log(data)

        // console.log(data.results)
    }

    return (
        <div className="workoutplan-search">
            <SearchBar
                placeholder="Search Workout Plan..."
                value={searchQuery}
                onChange={handleSearchChange}
                onSearch={handleSearch}
            />
        </div>
    )
}

export default WorkoutPlanSearchBar