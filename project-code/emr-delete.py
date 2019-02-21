import subprocess

def emr_delete(cid):

     subprocess.run("aws emr terminate-clusters --cluster-ids " + cid, shell=True)

     c_status = ("http://ec2-18-191-50-79.us-east-2.compute.amazonaws.com:8080/api/emr/info/" + cid)

     rtn_dict =   {
         "ClusterId": cid,
         "Status": "TERMINATING",
         "CheckClusterStatus": c_status
     }

     return rtn_dict
      
