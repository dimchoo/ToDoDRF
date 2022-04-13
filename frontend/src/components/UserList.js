const UserItem = ({user}) => {
    return(
        <tbody>
        <tr>
            <td>{user.id}</td>
            <td>{user.username}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
            <td>{user.phone_number}</td>
        </tr>
        </tbody>
    )
}

const UserList = ({users}) => {
    return(
        <table>
            <th>ID</th>
            <th>User Name</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Phone</th>
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}

export default UserList