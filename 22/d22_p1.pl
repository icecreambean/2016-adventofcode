#!/usr/bin/perl
# (answer is 950)
# ** initially used excel to find this answer, as suggested
#    on the reddit page :/

# needs O(n^2), no optimisation to calculate pairs correctly
# ((had issues from incorrect optimisations))

use warnings;
use strict;

# size/used/avail in units T; use as %
use constant { NAME => 0, SIZE => 1, USED => 2,
               AVAIL => 3, USE => 4 };
my @nodes = ();

# read input
my $i = 0;
open(my $fh, "<", "in.txt") or die "$!";
while (my $line = <$fh>) {
    $i++;
    next if ($i <= 2); # skip first two lines
    # don't require chomp
    #my ($name, $size, $used, $avail, $use) =
    my @node = $line =~ /(.*?)\s*(\d*)T\s*(\d*)T\s*(\d*)T\s*(\d*)%/;
    # insert reference to array to array (avoids flattening)
    push(@nodes, \@node );
}
close($fh);

# make pairs (order A,B)
my $n_pairs = num_pairs(\@nodes);
#my @nodes_reversed = reverse(@nodes); # wrong??
#$n_pairs += num_pairs(\@nodes_reversed);
print("part 1: ", $n_pairs, "\n");

# make pairs (order B,A): iterate through list backwards

# TODO: requires a visited list?? - no dup pairs???
sub num_pairs {
    my ($nodes_ref) = $_[0];
    my @nodes = @$nodes_ref;
    my $count = 0;
    foreach my $n1_ref (@nodes) {
        my @n1 = @$n1_ref; # references
        #for (my $i = 0; $i < scalar(@nodes); $i++) {
        #my $n1_ref = $nodes[$i];
        #my @n1 = @$n1_ref;
        if (scalar($n1[USED]) == 0) { # scalar() unnecessary
            next;
        }
        #foreach my $n2_ref (@nodes[$i..$#nodes]) { # splicing
        foreach my $n2_ref (@nodes) {
            my @n2 = @$n2_ref;
            next if $n1[NAME] eq $n2[NAME]; # ((important!!))
            # require n1 to fit on n2 (A on B)
            #if ($n1[USED] + $n2[USED] <= $n2[SIZE]) {
            if ($n1[USED] <= $n2[AVAIL]) {
                $count++;
            }
        }
    }
    return $count;
}

#print_nodes(\@nodes); # debugging usage
sub print_nodes {
    my ($nodes_ref) = $_[0];
    # each reference in array
    foreach my $node_ref (@$nodes_ref) {
        print(join(' ', @$node_ref),"\n");
    }
}

#http://stackoverflow.com/questions/16949013/perl-foreach-through-multidimensional-array
