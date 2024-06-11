
// Server Program : dnss.c

#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<string.h>
#include<errno.h>
#include<netdb.h>

int main()
{
    
    struct sockaddr_in server,client;
    int s,n;
    char b1[100],b2[100];

struct hostent *hen;
char *IPaddr;

    s=socket(AF_INET,SOCK_DGRAM,0);
    server.sin_family=AF_INET;
    server.sin_port=5000;
    server.sin_addr.s_addr=inet_addr("127.0.0.1");
    bind(s,(struct sockaddr *)&server,sizeof(server));
    n=sizeof(client);
 printf("DNS is ready ..\n");
    while(1)
    {

        strcpy(b2,"");
        recvfrom(s,b1,sizeof b1, 0,(struct sockaddr *)&client,&n);
       
       hen = gethostbyname(b1);

       printf("\n Client request for Domain Name: %s \n",hen->h_name); 
	IPaddr=inet_ntoa(*((struct in_addr *)hen->h_addr));

	printf("DNS IP address is:%s \n",IPaddr);
	strcpy(b2, IPaddr);

	sendto(s,b2,sizeof b2,0,(struct sockaddr *)&client,n); 
   }
return 0;
}

/*
> gcc dnss.c

./a.out
DNS is ready ..

 Client request for Domain Name: google.com 
DNS IP address is:142.250.193.142 

 Client request for Domain Name: uvce.ac.in 
DNS IP address is:134.209.146.145 

 Client request for Domain Name: netflix.com 
DNS IP address is:54.246.79.9 

 Client request for Domain Name: wikipedia.com 
DNS IP address is:103.102.166.226 


*/


// Client Program : dnsc.c

#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<netinet/in.h>
int main()
{
    struct sockaddr_in server,client;
    int s,n;
    char b1[100],b2[100];
    s=socket(AF_INET,SOCK_DGRAM,0);
    server.sin_family=AF_INET;
    server.sin_port=5000;
    server.sin_addr.s_addr=inet_addr("127.0.0.1");
    n=sizeof(server);
	
while(1){
    printf("\nEnter canonical Domain Name: ");
    scanf("%s",b2);
    sendto(s,b2,sizeof(b2),0,(struct sockaddr *)&server,n);
    recvfrom(s,b1,sizeof(b1), 0,NULL,NULL);
    printf("%s \n",b1);
}
return 0;
}

/*
> gcc dnsc.c
> ./a.out

Enter canonical Domain Name: google.com
142.250.193.142 

Enter canonical Domain Name: uvce.ac.in
134.209.146.145 

Enter canonical Domain Name: netflix.com
54.246.79.9 



//Dijkstra

#include<iostream>
#include<vector>
#include<set>
#include<climits>
using namespace std;

vector<pair<int, vector<int>>> dijkstra(int V, vector<vector<pair<int, int>>> &adj, int S) {
    vector<int> dist(V, INT_MAX);
    vector<vector<int>> paths(V);
    dist[S] = 0;

    set<pair<int, int>> st;
    st.insert({0, S});
    paths[S].push_back(S);

    while (!st.empty()) {
        auto it = *st.begin();
        int dis = it.first;
        int node = it.second;
        st.erase(it);

        for (auto adjIt : adj[node]) {
            int adjNode = adjIt.first;
            int wt = adjIt.second;

            if (dis + wt < dist[adjNode]) {
                auto f = st.find({dist[adjNode], adjNode});
                if (f != st.end()) {
                    st.erase(f);
                }
                
                dist[adjNode] = dis + wt;
                st.insert({dist[adjNode], adjNode});
                
                paths[adjNode] = paths[node];
                paths[adjNode].push_back(adjNode);
            }
        }
    }

    vector<pair<int, vector<int>>> result(V);
    for (int i = 0; i < V; ++i) {
        result[i] = {dist[i], paths[i]};
    }
    return result;
}

int main() {
    int V = 6;
    vector<vector<pair<int, int>>> adj(V);

    // Adding edges (node, weight)
    adj[0].push_back({1, 4});
    adj[0].push_back({2, 4});
    adj[1].push_back({2, 2});
    adj[1].push_back({0, 4});
    adj[2].push_back({3, 3});
    adj[2].push_back({5, 6});
    adj[2].push_back({4, 1});
    adj[3].push_back({2, 3});
    adj[3].push_back({5, 2});
    adj[4].push_back({3, 1});
    adj[5].push_back({3, 2});
    adj[5].push_back({4, 3});

    vector<pair<int, vector<int>>> shortestPaths = dijkstra(V, adj, 0);

    for (int i = 0; i < V; ++i) {
        cout << "Node " << i << ": Distance = " << shortestPaths[i].first << ", Path = ";
        for (int node : shortestPaths[i].second) {
            cout << node << " ";
        }
        cout << endl;
    }

    return 0;
}





// CRC program
// video link 
// https://www.youtube.com/watch?v=oA_ZfzJyAnI
#include<iostream>
#include<bits/stdc++.h>
using namespace std;

string msg,gen;

string get_crc(string m){
    while(m.size() >= gen.size()){
        string temp;
        
        for(int i=0; i<gen.size(); i++){
            m[i]==gen[i]  ? m[i]='0' : m[i]='1';
        }
        cout<<"after xor with 0's: "<<m<<endl;

        int zeros=0;
        for(int i=0; m[i]!='1' && i != m.size(); i++){
            if(m[i] == '1'){
                break;
            }else{
                zeros++;
            }
        }

        for(int i=zeros; i<m.size(); i++){
            
            temp.push_back(m[i]);
        }
        m.clear();
        m = temp;
        cout<<"after xor without 0's: "<<m<<endl;
        cout<<endl;
    
    }

    return m;
}


int main(){

    cout<<"\t<------ Sender Side ------>"<<endl;
    cout<<"Enter the message to send: ";
    cin>>msg;

    cout<<"Enter the generator bits: ";
    cin>>gen;

    int msgLen = msg.size();
    int genLen = gen.size();

    string dividend = msg;
    for(int i=0; i<genLen-1; i++){
        dividend.push_back('0');
    }

    cout<<"\nAfter appending n-1 gen bits, msg is: "<<dividend<<endl;

    string crc = get_crc(dividend);
    string tmp;
    if(crc.size()<gen.size()-1){
        for(int i=0; i<gen.size()-crc.size()-1; i++){
            tmp.push_back('0');
        }
    }
    tmp.append(crc);
    string finalMsg = msg.append(tmp);
    cout<<"\nMessage after adding crc: "<<finalMsg<<endl;

    
    cout<<"\t<------ At receiver end ------>"<<endl;
    
    string sndMsg;
    cout<<"Enter original msg to send , you add any error for testing: ";
    cin>>sndMsg;

    string getcrc = get_crc(sndMsg);
    cout<<"after calculating crc at receiver end, crc is: "<<getcrc<<endl;
    int cnt=0;
    for(int i=0; i<getcrc.size(); i++){
        if(getcrc[i] != '0'){
            cnt++;
            break;
        }
    }

    if(cnt>0){
        cout<<"Error has been detected"<<endl;
    }else{
        cout<<"\nNo error occured!,\nYou have received correct data: "<<msg<<endl;
        
    }

    return 0;
}




// Dns
//////////////////	IMPLEMENT DNS	////////////

// Server Program : dnss.c

#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<string.h>
#include<errno.h>
#include<netdb.h>

int main()
{
    
    struct sockaddr_in server,client;
    int s,n;
    char b1[100],b2[100];

struct hostent *hen;
char *IPaddr;

    s=socket(AF_INET,SOCK_DGRAM,0);
    server.sin_family=AF_INET;
    server.sin_port=5000;
    server.sin_addr.s_addr=inet_addr("127.0.0.1");
    bind(s,(struct sockaddr *)&server,sizeof(server));
    n=sizeof(client);
 printf("DNS is ready ..\n");
    while(1)
    {

        strcpy(b2,"");
        recvfrom(s,b1,sizeof b1, 0,(struct sockaddr *)&client,&n);
       
       hen = gethostbyname(b1);

       printf("\n Client request for Domain Name: %s \n",hen->h_name); 
	IPaddr=inet_ntoa(*((struct in_addr *)hen->h_addr));

	printf("DNS IP address is:%s \n",IPaddr);
	strcpy(b2, IPaddr);

	sendto(s,b2,sizeof b2,0,(struct sockaddr *)&client,n); 
   }
return 0;
}

/*
> gcc dnss.c

./a.out
DNS is ready ..

 Client request for Domain Name: google.com 
DNS IP address is:142.250.193.142 

 Client request for Domain Name: uvce.ac.in 
DNS IP address is:134.209.146.145 

 Client request for Domain Name: netflix.com 
DNS IP address is:54.246.79.9 

 Client request for Domain Name: wikipedia.com 
DNS IP address is:103.102.166.226 


*/


// Client Program : dnsc.c

#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<netinet/in.h>
int main()
{
    struct sockaddr_in server,client;
    int s,n;
    char b1[100],b2[100];
    s=socket(AF_INET,SOCK_DGRAM,0);
    server.sin_family=AF_INET;
    server.sin_port=5000;
    server.sin_addr.s_addr=inet_addr("127.0.0.1");
    n=sizeof(server);
	
while(1){
    printf("\nEnter canonical Domain Name: ");
    scanf("%s",b2);
    sendto(s,b2,sizeof(b2),0,(struct sockaddr *)&server,n);
    recvfrom(s,b1,sizeof(b1), 0,NULL,NULL);
    printf("%s \n",b1);
}
return 0;
}

/*
> gcc dnsc.c
> ./a.out

Enter canonical Domain Name: google.com
142.250.193.142 

Enter canonical Domain Name: uvce.ac.in
134.209.146.145 

Enter canonical Domain Name: netflix.com
54.246.79.9 

Enter canonical Domain Name: wikipedia.com
103.102.166.226 

*/




// 5. Using TCP/IP sockets, write a client – server program to make the client 
send the file name and to make the server send back the contents of the 
requested file if present.
SERVER
#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include <stdlib.h>
#include<string.h>
void error(char *msg)
{
perror(msg);
exit(1);
}
int main(int argc,char *argv[])
{
int sockfd,newsockfd,portno,clilen,n,i=0;
 char buffer[256],c[2000],ch;
 struct sockaddr_in serv_addr,cli_addr;
 FILE *fd;
 if(argc < 2)
{
 fprintf(stderr,"ERROR,no port provided\n");
 exit(1);
 }
sockfd=socket(AF_INET,SOCK_STREAM,0);
 if(sockfd<0)
 error("ERROR opening socket");
 bzero((char*) &serv_addr,sizeof(serv_addr));
 portno=atoi(argv[1]);
 serv_addr.sin_family=AF_INET;
 serv_addr.sin_addr.s_addr=INADDR_ANY;
 serv_addr.sin_port=htons(portno);
 if(bind(sockfd,(struct sockaddr*)&serv_addr,sizeof(serv_addr))<0)
 error("ERROR on binding");
 listen(sockfd,5);
 clilen=sizeof(cli_addr);
 printf("SERVER:Waiting for client....\n");
newsockfd=accept(sockfd,(struct sockaddr*) &cli_addr,&clilen);

if(newsockfd<0)
 error("ERROR on accept");
 bzero(buffer,256);
 n=read(newsockfd,buffer,255);
 if(n<0)
 error("ERROR reading from socket");
 printf("SERVER:%s \n",buffer);
 if((fd=freopen(buffer,"r",stdin))!=NULL)
 {
 printf("SERVER:%s found! \n Transfering the contents ...\n",buffer);
 while((ch=getc(stdin))!=EOF)
 c[i++]=ch;
 c[i]='\0';
 printf("File content %s\n",c);
 n=write(newsockfd,c,1999);
 if(n<0)
 error("ERROR in writing to socket");
 }
 else
 {
 printf("SERVER:File not found!\n");
 n=write(newsockfd,"File not found!",15);
 if(n<0)
 error("ERROR writing to socket");
 }
 return 0;
}
CLIENT
#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<netdb.h>
#include<string.h>
#include <stdlib.h>
void error(char *msg)
{
perror(msg);
exit(0);
}
int main(int argc,char *argv[])
{
int sockfd,portno,n;
struct sockaddr_in serv_addr;
struct hostent *server;
char filepath[256],buf[3000];
if(argc < 3)
{
fprintf(stderr,"usage %s hostname port\n",argv[0]);
exit(0);
}
portno=atoi(argv[2]);
sockfd=socket(AF_INET,SOCK_STREAM,0);
if(sockfd<0)
error("\nerror in opening socket");
printf("\nclient online");
server=gethostbyname(argv[1]);
if(server==NULL)
{
fprintf(stderr,"error ,no such host");
exit(0);
}
printf("\n server online");
bzero((struct sockaddr_in *)&serv_addr,sizeof(serv_addr));
serv_addr.sin_family=AF_INET;
bcopy((char *)server->h_addr,(char *)&serv_addr.sin_addr.s_addr,server->h_length);
serv_addr.sin_port=htons(portno);
if(connect(sockfd,(struct sockaddr_in*)&serv_addr,sizeof(serv_addr))<0)
error("error writing to socket");
printf("\nclient:enter path with filename:\n");
scanf("%s",filepath);
n=write(sockfd,filepath,strlen(filepath));
if(n<0)
error("\nerror writing to socket");
bzero(buf,3000);
n=read(sockfd,buf,2999);
if(n<0)
error("\nerror reading to socket");
printf("\nclient:displaying from socket");
fputs(buf,stdout);
return 0;
}




// 7. Write a Program to implement sliding window protocol.
SENDER
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<netdb.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
#include<errno.h>
int main()
{
 int sock,bytes_received,connected,true=1,i=1,s,f=0,sin_size;
 char send_data[1024],data[1024],c,fr[30]=" ";
 struct sockaddr_in server_addr,client_addr;
 if((sock=socket(AF_INET,SOCK_STREAM,0))==-1)
 {
 perror("Socket not created");
 exit(1);
 }
 if(setsockopt(sock,SOL_SOCKET,SO_REUSEADDR,&true,sizeof(int))==-1)
 {
 perror("Setsockopt");
 exit(1);
 }
 server_addr.sin_family=AF_INET;
 server_addr.sin_port=htons(17000);
 server_addr.sin_addr.s_addr=INADDR_ANY;
 if(bind(sock,(struct sockaddr *)&server_addr,sizeof(struct sockaddr))==-1)
 {
 perror("Unable to bind");
 exit(1);
 }
 if(listen(sock,5)==-1)
 {
 perror("Listen");
 exit(1);
 }
 fflush(stdout);
sin_size=sizeof(struct sockaddr_in);
 connected=accept(sock,(struct sockaddr *)&client_addr,&sin_size);
 while(strcmp(fr,"exit")!=0)
 {
 printf("Enter Data Frame %d:(Enter exit for End):",i);
 scanf("%s",fr);
 send(connected,fr,strlen(fr),0);
 recv(sock,data,1024,0);
 if(strlen(data)!=0)
 printf("I got an acknowledgment : %s\n",data);
 fflush(stdout);
 i++;
 }
 close(sock);
 return(0);
}
RECEIVER
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<netdb.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
#include<errno.h>
int main()
{
 int sock,bytes_received,i=1;
 char receive[30];
 struct hostent *host;
 struct sockaddr_in server_addr;
host=gethostbyname("127.0.0.1");
 if((sock=socket(AF_INET,SOCK_STREAM,0))==-1)
 {
 perror("Socket not created");
 exit(1);
 }
 printf("Socket created");
 server_addr.sin_family=AF_INET;
 server_addr.sin_port=htons(17000);
 server_addr.sin_addr=*((struct in_addr *)host->h_addr);
 bzero(&(server_addr.sin_zero),8);
 if(connect(sock,(struct sockaddr *)&server_addr,sizeof(struct sockaddr))==-1)

{
 perror("Connect");
 exit(1);
 }
 while(1)
 {
 bytes_received=recv(sock,receive,20,0);
 receive[bytes_received]='\0';
 if(strcmp(receive,"exit")==0)
 {
 close(sock);
 break;
 }
 else
 {
 if(strlen(receive)<10)
 {
printf("\nFrame %d data %s received\n",i,receive);
send(0,receive,strlen(receive),0);
 }
 else
 {
send(0,"negative",10,0);
 }
 i++;
 }
}
 close(sock);
 return(0);
}




// 8. Write a program to implement FIFO-Client and FIFO-Server to transfer 
files.
SERVER
#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<unistd.h>
#define FIFO1_NAME "fifo1"
#define FIFO2_NAME "fifo2"
int main()
{
char p[100],f[100],c[300],ch;
int num,num2,f1,fd,fd2,i=0;
mknod(FIFO1_NAME,S_IFIFO |0666,0);
mknod(FIFO2_NAME,S_IFIFO |0666,0);
printf("\nSERVER ONLINE");
fd=open(FIFO1_NAME,O_RDONLY);
printf("client online\nwaiting for request\n\n");
while(1)
{
if((num=read(fd,p,100))==-1)
perror("\nread error");
else
{
p[num]='\0';
if((f1=open(p,O_RDONLY))<0)
{
printf("\nserver: %s not found",p);
exit(1);
}
else
{
 printf("\nserver:%s found \ntranfering the contents",p);
stdin=fdopen(f1,"r");
while((ch=getc(stdin))!=EOF)

c[i++]=ch;
c[i]='\0';
printf("\nfile contents %s\n ",c);
fd2=open(FIFO2_NAME,O_WRONLY);
if(num2=write(fd2,c,strlen(c))==-1)
perror("\ntranfer error");
else
printf("\nserver :tranfer completed");
}
exit(1);
}
}
}
CLIENT
#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<unistd.h>
#define FIFO1_NAME "fifo1"
#define FIFO2_NAME "fifo2"
int main()
{
 char p[100],f[100],c[3000];
 int num,num2,f1,fd,fd2;
 mknod(FIFO1_NAME,S_IFIFO|0666,0);
mknod(FIFO2_NAME,S_IFIFO|0666,0);
 printf("\n waiting for server...\n");
 fd=open(FIFO1_NAME,O_WRONLY);
 printf("\n SERVER ONLINE !\n CLIENT:Enter the path\n");
 while(gets(p),!feof(stdin))
 {
 if((num=write(fd,p,strlen(p)))==-1)
 perror("write error\n");
 else
 {
 printf("Waiting for reply....\n");
 fd2=open(FIFO2_NAME,O_RDONLY);
 if((num2=read(fd2,c,3000))==-1)
 perror("Transfer error!\n");
 else

{ 
printf("File recieved! displaying the contents:\n");
 if(fputs(c,stdout)==EOF)
 perror("print error\n");
 exit(1);
 }
 }
 }
}



//9. Using UDP Sockets write client server program to transfer files.
SERVER
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<netdb.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
void error(char *msg)
{
perror(msg);
exit(0);
}
int main(int argc, char *argv[])
{
int sock, length, fromlen, n;
struct sockaddr_in server;
struct sockaddr_in from;
char buf[1024];
if (argc < 2)
{
fprintf(stderr, "ERROR, no port provided\n");
exit(0);
}
Sock=socket(AF_INET, SOCK_DGRAM, 0);
if (sock < 0)
{
error("Opening socket");
}
length = sizeof(server);
bzero(&server,length);
server.sin_family=AF_INET;
server.sin_addr.s_addr=INADDR_ANY;
server.sin_port=htons(atoi(argv[1]));
if (bind(sock,(struct sockaddr *)&server,length)<0)
{
error("binding");
}
fromlen = sizeof(struct sockaddr_in);
while (1)
{
n = recvfrom(sock,buf,1024,0,(struct sockaddr *)&from,&fromlen);

if (n < 0)
{
error("recvfrom");
}
write(1,"Received a datagram: ",21);
write(1,buf,n);
n = sendto(sock,"Got your message\n",17,
0,(struct sockaddr *)&from,fromlen);
if (n < 0)
{
error("sendto");
}
}
}
CLIENT
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<netdb.h>
#include<stdio.h>
#include<string.h>
#include <stdlib.h>
void error(char *);
int main(int argc, char *argv[])
{
int sock, length, n;
 struct sockaddr_in server, from;
 struct hostent *hp;
 char buffer[256];
 if (argc != 3)
{
 printf("Usage: server port\n");
 exit(1);
 }
 sock= socket(AF_INET, SOCK_DGRAM, 0);
if(sock<0)
 {
 error("socket");
 }
 server.sin_family=AF_INET;
hp=gethostbyname(argv[1]);

if(hp==0)
 {
 error("Unknown host");
}
 bcopy((char *)hp->h_addr,(char *)&server.sin_addr,hp->h_length);
 server.sin_port = htons(atoi(argv[2]));
 length=sizeof(struct sockaddr_in);
printf("Please enter the message: ");
 bzero(buffer,256);
 fgets(buffer,255,stdin);
 n=sendto(sock,buffer,strlen(buffer),0,&server,length);
 if (n < 0)
 {
 error("Sendto");
 }
n = recvfrom(sock,buffer,256,0,&from, &length);
if (n < 0)
 {
 error("recvfrom");
 }
 write(1,"Got an ack: ",12);
 write(1,buffer,n);
}
void error(char *msg)
{
 perror(msg);
 exit(0);
}






// 11.Write a program to implement Congestion Control using leaky bucket.
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/types.h>
#include<error.h>
#include<sys/stat.h>
#include<unistd.h>
#define min(x,y)((x)<(y)?(x):(y))
#define max(x,y)((x)>(y)?(x):(y))
#define MAX 25
int main()
{
 int cap,oprt,cont,i=0,inp[MAX],ch,nsec,drop;
 printf("LEAKY BUCKET ALGORITM\n");
 printf("\nEnter the bucket size:\n");
 scanf("%d",&cap);
 printf("\nEnter the output rate:");
 scanf("%d",&oprt);
 do
 {
 printf("\nEnter the number of packets entering at %d seconds\n",i+1);
 scanf("%d",&inp[i]);
 i++;
 printf("\nEnter 1 to insert packet or 0 to quit\n");
 scanf("%d",&ch);
 }
 while(ch);
 nsec=i;
 printf("\n(SECOND):(PACK RECVD):(PACK SENT):(PACK LEFT IN BUCKET):(PACK 
dROPPED)\n");
 cont=0;
 drop=0;
 for(i=0;i<nsec;i++)
 {
 cont+=inp[i];
 if(cont>cap)
 {
 drop=cont-cap;
 cont=cap;
 }
 printf("(%d): ",i+1);
printf("\t\t(%d): ",inp[i]);

 printf("\t\t(%d): ",min(cont,oprt));
 cont=cont-min(cont,oprt);
 printf("\t\t(%d)",cont);
 printf("\t\t(%d)\n",drop);
 }
 for(;cont!=0;i++)
 {
 if(cont>cap)
 cont=cap;
 drop=0;
 printf("(%d): ",i+1);
 printf("\t\t(0): ");
 printf("\t\t(%d): ",min(cont,oprt));
 cont=cont-min(cont,oprt);
 printf("\t\t(%d)",cont);
 printf("\t\t(%d)\n",drop);
 }
 return(0);
}



Enter canonical Domain Name: wikipedia.com
103.102.166.226 

*/
