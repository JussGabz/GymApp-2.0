// Re-usable SearchBar Component
const SearchBar = ({ onSearch }) => (
    <form onSubmit={(e) => { e.preventDefault(); onSearch(); }}>
        <div className='input-group mb-3'>
            <input
                type='text'
                className='form-control'
                placeholder='Search workout plans'
                onChange={(e) => onSearch(e.target.value)}
            />
            {/* <button className='btn btn-outline-secondary' type='submit'>Search</button> */}
        </div>
    </form>
)

export default SearchBar;