import {Link} from "react-router-dom";

const ProjectItem = ({project}) => {
    return(
        <tbody>
        <tr>
            <td><Link to={`/project/${project.id}`}>{project.name}</Link></td>
        </tr>
        </tbody>
    )
}

const ProjectList = ({projects}) => {
    return(
        <table>
            <th>Name</th>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}

export default ProjectList