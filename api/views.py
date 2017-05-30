from rest_framework.response import Response
from rest_framework import viewsets, status

from . import serializers
from . import Task,Interface


# Global variable used for the sake of simplicity.
# In real life, you'll be using your own interface to a data store
# of some sort, being caching, NoSQL, LDAP, external API or anything else
tasks = {
    1: Task(id=1, name='Demo'),
    2: Task(id=2, name='Model less demo'),
    3: Task(id=3, name='Sleep more'),
}


def get_next_task_id():
    return max(tasks) + 1

class ConfigViewSet(viewsets.ViewSet):
    serializer_class=serializers.ConfigSerializer
    def list(self, request,parent_lookup_id=None):
        # serializer = serializers.TaskSerializer(
        #     instance=tasks.values(), many=True)
        # serializer=serializer.config
        task = tasks[int(parent_lookup_id)]
        serializer=serializers.ConfigSerializer(task.config)
        return Response(serializer.data)
    def retrieve(self,request,pk=None,parent_lookup_id=None):
        try:
            task = tasks[int(parent_lookup_id)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer=serializers.ConfigSerializer(task.config)
        return Response(serializer.data[pk])
    def update(self, request, pk=None,parent_lookup_id=None):
        try:
            task = tasks[int(parent_lookup_id)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.InterfaceSerializer(
            data=request.data)
        if serializer.is_valid():
            task.config=Interface(**request.data)
            print(request.data['name'])
            # interface = serializer.save()
            # tasks[interface.name] = task
            # print(task.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TaskViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.TaskSerializer

    def list(self, request):
        serializer = serializers.TaskSerializer(
            instance=tasks.values(), many=True)
        print("list")
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            task.id = get_next_task_id()
            tasks[task.id] = task
            print("create")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            task = tasks[int(pk)]
            print("retrieve")
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(instance=task)
        #print("data in rerive :",serializer.data['config']['interface'])
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(
            data=request.data, instance=task)
        if serializer.is_valid():
            task = serializer.save()
            tasks[task.id] = task
            print("update")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, id=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(
            data=request.data,
            instance=task,
            partial=True)
        if serializer.is_valid():
            task = serializer.save()
            tasks[task.id] = task
            print("partial_update")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        del tasks[task.id]
        print("destroy")
        return Response(status=status.HTTP_204_NO_CONTENT)

# class InterfaceViewSet(viewsets.ViewSet):
#     serializer_class=InterfaceSerializer()
#     def retrieve(self, request, pk=None):
#         try:
#             task = tasks[int(pk)]
#             print("InterfaceViewSet :  retrieve")
#         except KeyError:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         except ValueError:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         serializer = serializers.TaskSerializer(instance=task)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         try:
#             task = tasks[int(pk)]
#         except KeyError:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         except ValueError:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         serializer = serializers.TaskSerializer(
#             data=request.data, instance=task)
#         if serializer.is_valid():
#             task = serializer.save()
#             tasks[task.id] = task
#             print("update")
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, config=None):
#         try:
#             task = tasks[int(pk)]
#         except KeyError:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         except ValueError:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         serializer = serializers.TaskSerializer(
#             data=request.data,
#             instance=task,
#             partial=True)
#         if serializer.is_valid():
#             task = serializer.save()
#             tasks[task.id] = task
#             print("partial_update")
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         try:
#             task = tasks[int(pk)]
#         except KeyError:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         except ValueError:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         del tasks[task.id]
#         print("destroy")
#         return Response(status=status.HTTP_204_NO_CONTENT)