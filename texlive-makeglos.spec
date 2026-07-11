%global tl_name makeglos
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Include a glossary into a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makeglos
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makeglos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makeglos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to include a glossary into a document.
The glossary is prepared by an external program, such as xindy or
makeindex, in the same way that an index is made.

