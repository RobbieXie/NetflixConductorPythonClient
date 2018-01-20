from __future__ import print_function

from conductor import conductor
import json


def registerTask(metadataClient,taskArr):
    metadataClient.registerTaskDefs(taskArr)

def unregisterTask(metadataClient,taskName):
    metadataClient.unRegisterTaskDef(taskName)

def main():
    print('Tiandi Workflow')
    metadataClient = conductor.MetadataClient('http://10.60.38.173:18080/api')
    workflowClient = conductor.WorkflowClient('http://10.60.38.173:18080/api')

    tasks = metadataClient.getAllTaskDefs()

    with open("mockJson/mockTask.json", 'r') as load_mockTask:
        taskJsonObj = json.load(load_mockTask)
        print(taskJsonObj)
        for (k,v) in taskJsonObj.items():
            print(k)
            print(v)
            registerTask(metadataClient, v)

    # ----- tiandi demo for unregisterTask -----
    # for (k, v) in taskJsonObj.items():
    #     for item in v:
    #         unregisterTask(metadataClient,item['name'])

    with open("mockJson/mockMetadata.json", 'r') as load_mockMetadata:
        metadataJsonArr = json.load(load_mockMetadata)
        for item in metadataJsonArr:
            try:
                metadataClient.createWorkflowDef(item)
            except Exception as err:
                print(err)
            workflowClient.startWorkflow(item['name'],{'inputString':'xietiandi666'})


if __name__ == '__main__':
    main()