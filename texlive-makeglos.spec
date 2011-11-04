# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/makeglos
# catalog-date 2007-02-23 00:16:39 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-makeglos
Version:	20070223
Release:	1
Summary:	Include a glossary into a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makeglos
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeglos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeglos.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides the means to include a glossary into a
document. The glossary is prepared by an external program, such
as xindy or makeindex, in the same way that an index is made.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makeglos/makeglos.sty
%doc %{_texmfdistdir}/doc/latex/makeglos/README
%doc %{_texmfdistdir}/doc/latex/makeglos/makeglos.pdf
%doc %{_texmfdistdir}/doc/latex/makeglos/makeglos.tex
%doc %{_texmfdistdir}/doc/latex/makeglos/makeglos.xdy
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
