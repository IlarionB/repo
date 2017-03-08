#!/usr/bin/python

from os import system
from time import sleep



def splash():
    system('clear')
    print "welcome to the boot order game\n"
    raw_input("press enter to continue\n")
    questions()

def questions():
    first = raw_input("what is the first stage\n")
    if first.lower() == 'bios':
        print "correct\n"
        print "bios is blah bla\n"

        second = raw_input("What is the second stage\n")
        if second.lower() == 'mbr':
            print "correct\n"
            print "mbr is blah blah blah\n"

            third = raw_input("What is the third level\n")
            if third.lower() == 'grub':
                print "correct\n"
                print "grub is blah blah\n"

                fourth = raw_input("What is the fourth level \n")
                if fourth.lower() == 'kernel':
                    print "correct\n"
                    print "kernel is blah blah\n"

                    fifth = raw_input("what is the fifth level \n")
                    if fifth.lower() == 'init':
                        print "correct\n"
                        print "init is blah blah blah\n"

                        sixth = raw_input("What is the sixth level \n")
                        if sixth.lower() == 'runlevels':
                            print "correct\n"
                            print "runlevels is blah blah bla\n"

                        else: wrong()
                    else: wrong()
                else: wrong()
            else: wrong()
        else: wrong()
    else: wrong()

def wrong():
    print "WRONG, restarting"
    sleep(3)
    splash()

splash()
