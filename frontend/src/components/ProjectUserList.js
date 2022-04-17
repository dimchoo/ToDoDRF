import {Link} from "react-router-dom";

const ProjectUserItem = ({project_user}) => {
    return(
        <tbody>
        <tr>
            <td>{project_user.id}</td>
            <td><Link to={`/project/${project_user.project}`}>{project_user.project}</Link></td>
            <td><Link to={`/user/${project_user.user}`}>{project_user.user}</Link></td>
        </tr>
        </tbody>
    )
}

const ProjectUserList = ({project_users}) => {
    return(
        <table>
            <th>ID</th>
            <th>Project</th>
            <th>User</th>
            {project_users.map((project_user) => <ProjectUserItem project_user={project_user}/>)}
        </table>
    )
}

export default ProjectUserList