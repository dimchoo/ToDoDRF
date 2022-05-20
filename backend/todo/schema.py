import graphene
from graphene_django import DjangoObjectType
from todo.models import Project, Task, ProjectUser


class ProjectUserType(DjangoObjectType):
    class Meta:
        model = ProjectUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_tasks = graphene.List(TaskType)
    project_by_id = graphene.Field(ProjectType, pk=graphene.Int(required=True))

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_project_by_id(self, info, pk):
        return Project.objects.get(pk=pk)

    def resolve_all_tasks(self, info):
        return Task.objects.all()


class ProjectCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        repo_link = graphene.String(required=False)
        description = graphene.String(required=False)
        created_by = graphene.ID(required=True)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, created_by, repo_link=None, description=None):
        project = Project(name=name, created_by_id=created_by, repo_link=repo_link, description=description)
        project.save()
        return cls(project)


class ProjectUpdateMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.Int(required=True)
        name = graphene.String(required=False)
        repo_link = graphene.String(required=False)
        description = graphene.String(required=False)
        created_by = graphene.ID(required=False)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, pk, **kwargs):
        project = Project.objects.get(pk=pk)
        if kwargs:
            for k, v in kwargs.items():
                setattr(project, k, v)
            project.save()
        return cls(project)


class Mutation(graphene.ObjectType):
    create_project = ProjectCreateMutation.Field()
    update_project = ProjectUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
