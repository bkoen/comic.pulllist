#!/bin/env perl
############################ use mods #################################################
use strict;
use warnings;
use Data::Dumper;
use LWP::Simple;
########################################################################################
##################### Download newreleases.txt from previewsworld.com ##################
my $url = 'http://www.previewsworld.com/shipping/newreleases.txt';
my $localfile = './newreleases.txt';
getstore($url, $localfile);
########################################################################################
############# Read newreleases.txt and store each line in @books #######################
open my $newreleases,"<", "./newreleases.txt"
	or die "can not open newreleases.txt\n";

my $line;
my @books;
while ($line = <$newreleases>) 
	{
	push(@books, lc($line))
	}
close($newreleases);
#######################################################################################
########### Read wanted.txt and store each line in @pulllist ##########################
open my $wanted,"<", "./wanted.txt"
	or die "can not open wanted.txt\n";
	
my $title;
my @pulllist;
while ($title = <$wanted>)
	{
	chomp($title);
	push(@pulllist, $title)
	}
close($wanted);
########################################################################################
################# Compare @pulllist and @books and store matches in @avail #############

my $title2;
my $fullline;
my @avail;
foreach $title2	(@pulllist)
{
	if (grep /$title2/, @books)
	{
	push(@avail, (grep /$title2/, @books))
	}
}
########################################################################################
########################## print final list ############################################
print @avail;
########################################################################################

