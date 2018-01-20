from conductor import conductor

serverUrl = 'http://10.60.38.173:18080/api'

clientMgr = conductor.WFClientMgr(serverUrl)
metadataClient = clientMgr.metadataClient
taskClient = clientMgr.taskClient
workflowClient = clientMgr.workflowClient

# task
def getTask(taskName = None):
    if taskName == None:
        return metadataClient.getAllTaskDefs()
    else:
        return metadataClient.getTaskDef(taskName)

def registerTask(taskArr):
    return metadataClient.registerTaskDefs(taskArr)

def updateTask(taskArr):
    return metadataClient.registerTaskDefs(taskArr)

def unregisterTask(taskName):
    return metadataClient.unRegisterTaskDef(taskName)


# metadata
def getMetadata(wfName = None):
    if wfName == None:
        return metadataClient.getAllWorkflowDefs();
    else:
        return metadataClient.getWorkflowDef(wfName)

def createMetadata(wfdObj):
    return metadataClient.createWorkflowDef(wfdObj)

def updateMetadata(wfdObjArr):
    return metadataClient.updateWorkflowDefs(wfdObjArr)


# workflow
def startWorkflow(wfName,inputjson):
    return workflowClient.startWorkflow(wfName,inputjson)

def getWorkflowById(wfId):
    return workflowClient.getWorkflow(wfId)

def getRunningWorkflowsByName(wfName):
    return workflowClient.getRunningWorkflows(wfName)

