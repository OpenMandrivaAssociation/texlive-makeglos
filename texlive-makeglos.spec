Name:		texlive-makeglos
Version:	15878
Release:	2
Summary:	Include a glossary into a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makeglos
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeglos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeglos.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to include a glossary into a
document. The glossary is prepared by an external program, such
as xindy or makeindex, in the same way that an index is made.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makeglos/makeglos.sty
%doc %{_texmfdistdir}/doc/latex/makeglos/README
%doc %{_texmfdistdir}/doc/latex/makeglos/makeglos.pdf
%doc %{_texmfdistdir}/doc/latex/makeglos/makeglos.tex
%doc %{_texmfdistdir}/doc/latex/makeglos/makeglos.xdy

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
