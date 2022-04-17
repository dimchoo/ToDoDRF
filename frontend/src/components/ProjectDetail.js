import {useParams, Link} from "react-router-dom";

const ProjectDetail = ({projects}) => {
    let {id} = useParams();
    const project = projects.find((p) => p.id === Number(id));
    return(
        <div>
            <div>ID: {project.id}</div>
            <div>Name: {project.name}</div>
            <div>Repo: {project.repo_link}</div>
            <div>Desc: {project.description}</div>
            <div>Created by: <Link to={`/project-users/${project.created_by}`}>{project.created_by}</Link></div>
        </div>
    )
}
export default ProjectDetail