import boto3

def emr_get(cid):

     client = boto3.client('emr')
     c_info = client.describe_cluster(ClusterId=cid)

     c_status = c_info["Cluster"]["Status"]["State"]
     if "MasterPublicDnsName" in c_info["Cluster"]:
          j_hub = ("https://" + c_info["Cluster"]["MasterPublicDnsName"] + ":9443")
          j_un = "jovyan"
          j_pw = "jupyter"
     else:
          j_hub = ""
          j_un = ""
          j_pw = ""

     rtn_dict = {
          "ClusterId": cid,
          "ClusterStatus": c_status,
          "JupyterHub": j_hub,
          "JupyterUN": j_un,
          "JupyterPW": j_pw
     }
 
     return rtn_dict

response = client.list_clusters(ClusterStates=['STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING'])
