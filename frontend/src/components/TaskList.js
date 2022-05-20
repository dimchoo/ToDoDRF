const TaskItem = ({task, deleteTask}) => {
    return(
        <tbody>
        <tr>
            <td>{task.id}</td>
            <td>{task.name}</td>
            <td>{task.project}</td>
            <td>{task.description}</td>
            <td>{task.created_by}</td>
            <td>{task.users}</td>
            <td>{task.status}</td>
            <td>{task.deadline}</td>
            <td><button onClick={ ()=> deleteTask(task.id)}>Delete</button></td>
        </tr>
        </tbody>
    )
}

const TaskList = ({tasks, users, deleteTask}) => {
    return(
        <table>
            <th>ID</th>
            <th>Name</th>
            <th>Project</th>
            <th>Description</th>
            <th>Created by</th>
            <th>Users</th>
            <th>Status</th>
            <th>Deadline</th>
            {tasks.map((task) => <TaskItem task={task} users={users} deleteTask={deleteTask}/>)}
        </table>
    )
}

export default TaskList