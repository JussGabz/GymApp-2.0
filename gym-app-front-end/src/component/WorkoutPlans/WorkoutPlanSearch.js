import React, { useState } from "react";
import SearchBar from "../../genericSearchBar";
import { fetchWorkoutPlans } from "../../services/workoutplanService";

function WorkoutPlanSearchBar() {
    const [searchQuery, setSearchQuery] = useState('')

    const handleSearchChange = (newValue) => {
        setSearchQuery(newValue)
    }

    const handleSearch = async (query) => {
        console.log(`Searching for: ${query}`)

        const data = await fetchWorkoutPlans()

        console.log(data.results)
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