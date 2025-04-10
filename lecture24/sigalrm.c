/* sigalrm.c: An example of using alarm */

#include <errno.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <unistd.h>

bool Wakeup = false;

void sigalrm_handler(int signum) {
    Wakeup = true;
}

int main(int argc, char *argv[]) {
    int timeout = atoi(argv[1]);

    signal(SIGALRM, sigalrm_handler);   // Register handler
    				    
    alarm(timeout);			// Set alarm

    // Print out message while waiting for alarm to trigger
    int seconds = 1;
    while (!Wakeup) {
    	printf("\r%d. Waiting...", seconds++);
    	fflush(stdout);
    	sleep(1);
    }
    
    // Print out alarm
    printf("\r!!! WAKE UP !!!\n");

    return EXIT_SUCCESS;
}

/* vim: set sts=4 sw=4 ts=8 expandtab ft=c: */
