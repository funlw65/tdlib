## Process this file with automake to produce Makefile.in
#
# Makefile.am
#
# Automake input file.
#
# Copyright (C) 2016 Felix Salfelder
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this package; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street - Fifth Floor,
# Boston, MA 02110-1301, USA.
#

SUBDIRS = gr

AM_DEFAULT_SOURCE_EXT = .cc

if USE_GALA
GALA_NOINST_APPS = \
	tdecomp-profile
GALA_APPS = \
	tdecomp
endif

BOOST_LIBS = -lboost_thread -lboost_system -lpthread

PROFILE_GEN = -fprofile-generate
PROFILE_FLAGS = -fprofile-use=.
PROFILE_GRAPH = gr/h.gr

COMMON_CXXFLAGS = -Os -march=native

tdecompdir=$(pkglibexecdir)

if !CLANG
tdecomp_PROGRAMS = ${GALA_APPS}
check_PROGRAMS = ${GALA_NOINST_APPS} td-validate
endif

td_validate_CPPFLAGS=${AM_CPPFLAGS} -I${top_srcdir}/src

if TDECOMP
TDECOMP_TESTS = test-fi.sh test-ppfi.sh
endif

TESTS = ${TDECOMP_TESTS}

tdecomp_profile_SOURCES = tdecomp.cc
tdecomp_profile_CXXFLAGS = $(AM_CXXFLAGS) $(PROFILE_GEN) $(COMMON_CXXFLAGS)
tdecomp_profile_CPPFLAGS = $(AM_CPPFLAGS) -I.
tdecomp_profile_LDADD = $(BOOST_LIBS) -lboost_graph

tdecomp_SOURCES = tdecomp.cc
tdecomp_CXXFLAGS = $(AM_CXXFLAGS) $(PROFILE_FLAGS) $(COMMON_CXXFLAGS)
tdecomp_CPPFLAGS = $(AM_CPPFLAGS) -I.
tdecomp_LDADD = $(BOOST_LIBS) -lboost_graph

# i forgot how to clean this up
GRTD_AMNAME = tdecomp-tdecomp
GRTDP_AMNAME = tdecomp_profile-tdecomp

# trial and error?!
$(TWEX_AMNAME).o: $(TWEXP_AMNAME).gcda
$(TWEX_AMNAME).Tpo: $(TWEXP_AMNAME).gcda
$(GRTD_AMNAME).o: $(GRTDP_AMNAME).gcda
$(GRTD_AMNAME).Tpo: $(GRTDP_AMNAME).gcda

TIME=1

$(GRTDP_AMNAME).gcda: $(PROFILE_GRAPH) tdecomp-profile
	rm -f $@
	@for i in --ex17 --fi --ppfi; do \
		echo "./tdecomp-profile -m $$i < $< > $<.td$$i & p=\$$!; sleep $(TIME); kill -TERM \$$p;"; \
		./tdecomp-profile -m $$i < $< > $<.i.td$$i & p=$$!; sleep $(TIME); kill -TERM $$p; \
      wait $$p; \
		grep -v incomplete $<.i.td$$i > $<.td$$i; \
		rm $<.i.td$$i; \
		td-validate $< $<.td$$i || : ; \
	done

BUILT_SOURCES = treedec
CLEANFILES = \
	${BUILT_SOURCES} *~ \
   $(TWEXP_AMNAME).gcda \
	$(GRTDP_AMNAME).gcda \
	HoffmanGraph.gr.td*

treedec:
	-$(LN_S) $(top_srcdir)/src $@

#here?
EXTRA_DIST = \
	${TESTS} \
	gala_graphs.h \
	grparse.h twthread.hpp twh.h \
	timer.h \
   ex17_thread.h \
   fi_thread.h \
   pp_thread.h \
   th_thread.h \
   bmd_thread.h

# TESTS = $(check_PROGRAMS)

# AM_DEFAULT_SOURCE_EXT=.cc

# AM_CPPFLAGS = -I. -DTRACE_UNTESTED
AM_CPPFLAGS = $(LOCAL_CPPFLAGS)
# AM_CXXFLAGS = -O0 -g
#
$(TESTS:%=%.log): .P
.PHONY: .P

.P:
	@:
