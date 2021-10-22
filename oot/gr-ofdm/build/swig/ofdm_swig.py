# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ofdm_swig
else:
    import _ofdm_swig

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def high_res_timer_now() -> "gr::high_res_timer_type":
    r"""high_res_timer_now() -> gr::high_res_timer_type"""
    return _ofdm_swig.high_res_timer_now()

def high_res_timer_now_perfmon() -> "gr::high_res_timer_type":
    r"""high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _ofdm_swig.high_res_timer_now_perfmon()

def high_res_timer_tps() -> "gr::high_res_timer_type":
    r"""high_res_timer_tps() -> gr::high_res_timer_type"""
    return _ofdm_swig.high_res_timer_tps()

def high_res_timer_epoch() -> "gr::high_res_timer_type":
    r"""high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _ofdm_swig.high_res_timer_epoch()
class pilot_comp_cc(object):
    r"""
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of ofdm::pilot_comp_cc.

    To avoid accidental use of raw pointers, ofdm::pilot_comp_cc's constructor is in a private implementation class. ofdm::pilot_comp_cc::make is the public interface for creating new instances.

    Args:
        fft_len : 
        apply_comp : 
        num_syms : 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def make(fft_len: "int", apply_comp: "int", num_syms: "int") -> "gr::ofdm::pilot_comp_cc::sptr":
        r"""
        make(int fft_len, int apply_comp, int num_syms) -> pilot_comp_cc_sptr
        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of ofdm::pilot_comp_cc.

        To avoid accidental use of raw pointers, ofdm::pilot_comp_cc's constructor is in a private implementation class. ofdm::pilot_comp_cc::make is the public interface for creating new instances.

        Args:
            fft_len : 
            apply_comp : 
            num_syms : 
        """
        return _ofdm_swig.pilot_comp_cc_make(fft_len, apply_comp, num_syms)

    def toggle_comp(self, apply_comp: "int") -> "void":
        r"""toggle_comp(pilot_comp_cc self, int apply_comp)"""
        return _ofdm_swig.pilot_comp_cc_toggle_comp(self, apply_comp)
    __swig_destroy__ = _ofdm_swig.delete_pilot_comp_cc

# Register pilot_comp_cc in _ofdm_swig:
_ofdm_swig.pilot_comp_cc_swigregister(pilot_comp_cc)

def pilot_comp_cc_make(fft_len: "int", apply_comp: "int", num_syms: "int") -> "gr::ofdm::pilot_comp_cc::sptr":
    r"""
    pilot_comp_cc_make(int fft_len, int apply_comp, int num_syms) -> pilot_comp_cc_sptr
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of ofdm::pilot_comp_cc.

    To avoid accidental use of raw pointers, ofdm::pilot_comp_cc's constructor is in a private implementation class. ofdm::pilot_comp_cc::make is the public interface for creating new instances.

    Args:
        fft_len : 
        apply_comp : 
        num_syms : 
    """
    return _ofdm_swig.pilot_comp_cc_make(fft_len, apply_comp, num_syms)

class pilot_comp_cc_sptr(object):
    r"""Proxy of C++ boost::shared_ptr< gr::ofdm::pilot_comp_cc > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(pilot_comp_cc_sptr self) -> pilot_comp_cc_sptr
        __init__(pilot_comp_cc_sptr self, pilot_comp_cc p) -> pilot_comp_cc_sptr
        """
        _ofdm_swig.pilot_comp_cc_sptr_swiginit(self, _ofdm_swig.new_pilot_comp_cc_sptr(*args))

    def __deref__(self) -> "gr::ofdm::pilot_comp_cc *":
        r"""__deref__(pilot_comp_cc_sptr self) -> pilot_comp_cc"""
        return _ofdm_swig.pilot_comp_cc_sptr___deref__(self)
    __swig_destroy__ = _ofdm_swig.delete_pilot_comp_cc_sptr

    def make(self, fft_len: "int", apply_comp: "int", num_syms: "int") -> "gr::ofdm::pilot_comp_cc::sptr":
        r"""
        make(pilot_comp_cc_sptr self, int fft_len, int apply_comp, int num_syms) -> pilot_comp_cc_sptr
        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of ofdm::pilot_comp_cc.

        To avoid accidental use of raw pointers, ofdm::pilot_comp_cc's constructor is in a private implementation class. ofdm::pilot_comp_cc::make is the public interface for creating new instances.

        Args:
            fft_len : 
            apply_comp : 
            num_syms : 
        """
        return _ofdm_swig.pilot_comp_cc_sptr_make(self, fft_len, apply_comp, num_syms)

    def toggle_comp(self, apply_comp: "int") -> "void":
        r"""toggle_comp(pilot_comp_cc_sptr self, int apply_comp)"""
        return _ofdm_swig.pilot_comp_cc_sptr_toggle_comp(self, apply_comp)

    def history(self) -> "unsigned int":
        r"""history(pilot_comp_cc_sptr self) -> unsigned int"""
        return _ofdm_swig.pilot_comp_cc_sptr_history(self)

    def declare_sample_delay(self, *args) -> "void":
        r"""
        declare_sample_delay(pilot_comp_cc_sptr self, int which, int delay)
        declare_sample_delay(pilot_comp_cc_sptr self, unsigned int delay)
        """
        return _ofdm_swig.pilot_comp_cc_sptr_declare_sample_delay(self, *args)

    def sample_delay(self, which: "int") -> "unsigned int":
        r"""sample_delay(pilot_comp_cc_sptr self, int which) -> unsigned int"""
        return _ofdm_swig.pilot_comp_cc_sptr_sample_delay(self, which)

    def set_output_multiple(self, multiple: "int") -> "void":
        r"""set_output_multiple(pilot_comp_cc_sptr self, int multiple)"""
        return _ofdm_swig.pilot_comp_cc_sptr_set_output_multiple(self, multiple)

    def output_multiple(self) -> "int":
        r"""output_multiple(pilot_comp_cc_sptr self) -> int"""
        return _ofdm_swig.pilot_comp_cc_sptr_output_multiple(self)

    def relative_rate(self) -> "double":
        r"""relative_rate(pilot_comp_cc_sptr self) -> double"""
        return _ofdm_swig.pilot_comp_cc_sptr_relative_rate(self)

    def relative_rate_i(self) -> "uint64_t":
        r"""relative_rate_i(pilot_comp_cc_sptr self) -> uint64_t"""
        return _ofdm_swig.pilot_comp_cc_sptr_relative_rate_i(self)

    def relative_rate_d(self) -> "uint64_t":
        r"""relative_rate_d(pilot_comp_cc_sptr self) -> uint64_t"""
        return _ofdm_swig.pilot_comp_cc_sptr_relative_rate_d(self)

    def start(self) -> "bool":
        r"""start(pilot_comp_cc_sptr self) -> bool"""
        return _ofdm_swig.pilot_comp_cc_sptr_start(self)

    def stop(self) -> "bool":
        r"""stop(pilot_comp_cc_sptr self) -> bool"""
        return _ofdm_swig.pilot_comp_cc_sptr_stop(self)

    def nitems_read(self, which_input: "unsigned int") -> "uint64_t":
        r"""nitems_read(pilot_comp_cc_sptr self, unsigned int which_input) -> uint64_t"""
        return _ofdm_swig.pilot_comp_cc_sptr_nitems_read(self, which_input)

    def nitems_written(self, which_output: "unsigned int") -> "uint64_t":
        r"""nitems_written(pilot_comp_cc_sptr self, unsigned int which_output) -> uint64_t"""
        return _ofdm_swig.pilot_comp_cc_sptr_nitems_written(self, which_output)

    def set_log_level(self, level: "std::string") -> "void":
        r"""set_log_level(pilot_comp_cc_sptr self, std::string level)"""
        return _ofdm_swig.pilot_comp_cc_sptr_set_log_level(self, level)

    def log_level(self) -> "std::string":
        r"""log_level(pilot_comp_cc_sptr self) -> std::string"""
        return _ofdm_swig.pilot_comp_cc_sptr_log_level(self)

    def max_noutput_items(self) -> "int":
        r"""max_noutput_items(pilot_comp_cc_sptr self) -> int"""
        return _ofdm_swig.pilot_comp_cc_sptr_max_noutput_items(self)

    def set_max_noutput_items(self, m: "int") -> "void":
        r"""set_max_noutput_items(pilot_comp_cc_sptr self, int m)"""
        return _ofdm_swig.pilot_comp_cc_sptr_set_max_noutput_items(self, m)

    def unset_max_noutput_items(self) -> "void":
        r"""unset_max_noutput_items(pilot_comp_cc_sptr self)"""
        return _ofdm_swig.pilot_comp_cc_sptr_unset_max_noutput_items(self)

    def is_set_max_noutput_items(self) -> "bool":
        r"""is_set_max_noutput_items(pilot_comp_cc_sptr self) -> bool"""
        return _ofdm_swig.pilot_comp_cc_sptr_is_set_max_noutput_items(self)

    def set_min_noutput_items(self, m: "int") -> "void":
        r"""set_min_noutput_items(pilot_comp_cc_sptr self, int m)"""
        return _ofdm_swig.pilot_comp_cc_sptr_set_min_noutput_items(self, m)

    def min_noutput_items(self) -> "int":
        r"""min_noutput_items(pilot_comp_cc_sptr self) -> int"""
        return _ofdm_swig.pilot_comp_cc_sptr_min_noutput_items(self)

    def max_output_buffer(self, i: "int") -> "long":
        r"""max_output_buffer(pilot_comp_cc_sptr self, int i) -> long"""
        return _ofdm_swig.pilot_comp_cc_sptr_max_output_buffer(self, i)

    def set_max_output_buffer(self, *args) -> "void":
        r"""
        set_max_output_buffer(pilot_comp_cc_sptr self, long max_output_buffer)
        set_max_output_buffer(pilot_comp_cc_sptr self, int port, long max_output_buffer)
        """
        return _ofdm_swig.pilot_comp_cc_sptr_set_max_output_buffer(self, *args)

    def min_output_buffer(self, i: "int") -> "long":
        r"""min_output_buffer(pilot_comp_cc_sptr self, int i) -> long"""
        return _ofdm_swig.pilot_comp_cc_sptr_min_output_buffer(self, i)

    def set_min_output_buffer(self, *args) -> "void":
        r"""
        set_min_output_buffer(pilot_comp_cc_sptr self, long min_output_buffer)
        set_min_output_buffer(pilot_comp_cc_sptr self, int port, long min_output_buffer)
        """
        return _ofdm_swig.pilot_comp_cc_sptr_set_min_output_buffer(self, *args)

    def pc_noutput_items(self) -> "float":
        r"""pc_noutput_items(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_noutput_items(self)

    def pc_noutput_items_avg(self) -> "float":
        r"""pc_noutput_items_avg(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_noutput_items_avg(self)

    def pc_noutput_items_var(self) -> "float":
        r"""pc_noutput_items_var(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_noutput_items_var(self)

    def pc_nproduced(self) -> "float":
        r"""pc_nproduced(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_nproduced(self)

    def pc_nproduced_avg(self) -> "float":
        r"""pc_nproduced_avg(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_nproduced_avg(self)

    def pc_nproduced_var(self) -> "float":
        r"""pc_nproduced_var(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_nproduced_var(self)

    def pc_input_buffers_full(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_input_buffers_full(pilot_comp_cc_sptr self, int which) -> float
        pc_input_buffers_full(pilot_comp_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.pilot_comp_cc_sptr_pc_input_buffers_full(self, *args)

    def pc_input_buffers_full_avg(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_input_buffers_full_avg(pilot_comp_cc_sptr self, int which) -> float
        pc_input_buffers_full_avg(pilot_comp_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.pilot_comp_cc_sptr_pc_input_buffers_full_avg(self, *args)

    def pc_input_buffers_full_var(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_input_buffers_full_var(pilot_comp_cc_sptr self, int which) -> float
        pc_input_buffers_full_var(pilot_comp_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.pilot_comp_cc_sptr_pc_input_buffers_full_var(self, *args)

    def pc_output_buffers_full(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_output_buffers_full(pilot_comp_cc_sptr self, int which) -> float
        pc_output_buffers_full(pilot_comp_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.pilot_comp_cc_sptr_pc_output_buffers_full(self, *args)

    def pc_output_buffers_full_avg(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_output_buffers_full_avg(pilot_comp_cc_sptr self, int which) -> float
        pc_output_buffers_full_avg(pilot_comp_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.pilot_comp_cc_sptr_pc_output_buffers_full_avg(self, *args)

    def pc_output_buffers_full_var(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_output_buffers_full_var(pilot_comp_cc_sptr self, int which) -> float
        pc_output_buffers_full_var(pilot_comp_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.pilot_comp_cc_sptr_pc_output_buffers_full_var(self, *args)

    def pc_work_time(self) -> "float":
        r"""pc_work_time(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_work_time(self)

    def pc_work_time_avg(self) -> "float":
        r"""pc_work_time_avg(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_work_time_avg(self)

    def pc_work_time_var(self) -> "float":
        r"""pc_work_time_var(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_work_time_var(self)

    def pc_work_time_total(self) -> "float":
        r"""pc_work_time_total(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_work_time_total(self)

    def pc_throughput_avg(self) -> "float":
        r"""pc_throughput_avg(pilot_comp_cc_sptr self) -> float"""
        return _ofdm_swig.pilot_comp_cc_sptr_pc_throughput_avg(self)

    def set_processor_affinity(self, mask: "std::vector< int,std::allocator< int > > const &") -> "void":
        r"""set_processor_affinity(pilot_comp_cc_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _ofdm_swig.pilot_comp_cc_sptr_set_processor_affinity(self, mask)

    def unset_processor_affinity(self) -> "void":
        r"""unset_processor_affinity(pilot_comp_cc_sptr self)"""
        return _ofdm_swig.pilot_comp_cc_sptr_unset_processor_affinity(self)

    def processor_affinity(self) -> "std::vector< int,std::allocator< int > >":
        r"""processor_affinity(pilot_comp_cc_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _ofdm_swig.pilot_comp_cc_sptr_processor_affinity(self)

    def active_thread_priority(self) -> "int":
        r"""active_thread_priority(pilot_comp_cc_sptr self) -> int"""
        return _ofdm_swig.pilot_comp_cc_sptr_active_thread_priority(self)

    def thread_priority(self) -> "int":
        r"""thread_priority(pilot_comp_cc_sptr self) -> int"""
        return _ofdm_swig.pilot_comp_cc_sptr_thread_priority(self)

    def set_thread_priority(self, priority: "int") -> "int":
        r"""set_thread_priority(pilot_comp_cc_sptr self, int priority) -> int"""
        return _ofdm_swig.pilot_comp_cc_sptr_set_thread_priority(self, priority)

    def name(self) -> "std::string":
        r"""name(pilot_comp_cc_sptr self) -> std::string"""
        return _ofdm_swig.pilot_comp_cc_sptr_name(self)

    def symbol_name(self) -> "std::string":
        r"""symbol_name(pilot_comp_cc_sptr self) -> std::string"""
        return _ofdm_swig.pilot_comp_cc_sptr_symbol_name(self)

    def input_signature(self) -> "gr::io_signature::sptr":
        r"""input_signature(pilot_comp_cc_sptr self) -> io_signature_sptr"""
        return _ofdm_swig.pilot_comp_cc_sptr_input_signature(self)

    def output_signature(self) -> "gr::io_signature::sptr":
        r"""output_signature(pilot_comp_cc_sptr self) -> io_signature_sptr"""
        return _ofdm_swig.pilot_comp_cc_sptr_output_signature(self)

    def unique_id(self) -> "long":
        r"""unique_id(pilot_comp_cc_sptr self) -> long"""
        return _ofdm_swig.pilot_comp_cc_sptr_unique_id(self)

    def to_basic_block(self) -> "gr::basic_block_sptr":
        r"""to_basic_block(pilot_comp_cc_sptr self) -> basic_block_sptr"""
        return _ofdm_swig.pilot_comp_cc_sptr_to_basic_block(self)

    def check_topology(self, ninputs: "int", noutputs: "int") -> "bool":
        r"""check_topology(pilot_comp_cc_sptr self, int ninputs, int noutputs) -> bool"""
        return _ofdm_swig.pilot_comp_cc_sptr_check_topology(self, ninputs, noutputs)

    def alias(self) -> "std::string":
        r"""alias(pilot_comp_cc_sptr self) -> std::string"""
        return _ofdm_swig.pilot_comp_cc_sptr_alias(self)

    def set_block_alias(self, name: "std::string") -> "void":
        r"""set_block_alias(pilot_comp_cc_sptr self, std::string name)"""
        return _ofdm_swig.pilot_comp_cc_sptr_set_block_alias(self, name)

    def _post(self, which_port: "swig_pmt_ptr", msg: "swig_pmt_ptr") -> "void":
        r"""_post(pilot_comp_cc_sptr self, swig_pmt_ptr which_port, swig_pmt_ptr msg)"""
        return _ofdm_swig.pilot_comp_cc_sptr__post(self, which_port, msg)

    def message_ports_in(self) -> "pmt::pmt_t":
        r"""message_ports_in(pilot_comp_cc_sptr self) -> swig_pmt_ptr"""
        return _ofdm_swig.pilot_comp_cc_sptr_message_ports_in(self)

    def message_ports_out(self) -> "pmt::pmt_t":
        r"""message_ports_out(pilot_comp_cc_sptr self) -> swig_pmt_ptr"""
        return _ofdm_swig.pilot_comp_cc_sptr_message_ports_out(self)

    def message_subscribers(self, which_port: "swig_pmt_ptr") -> "pmt::pmt_t":
        r"""message_subscribers(pilot_comp_cc_sptr self, swig_pmt_ptr which_port) -> swig_pmt_ptr"""
        return _ofdm_swig.pilot_comp_cc_sptr_message_subscribers(self, which_port)

# Register pilot_comp_cc_sptr in _ofdm_swig:
_ofdm_swig.pilot_comp_cc_sptr_swigregister(pilot_comp_cc_sptr)


pilot_comp_cc_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
pilot_comp_cc = pilot_comp_cc.make;

class alamouti_cc(object):
    r"""
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of ofdm::alamouti_cc.

    To avoid accidental use of raw pointers, ofdm::alamouti_cc's constructor is in a private implementation class. ofdm::alamouti_cc::make is the public interface for creating new instances.

    Args:
        p_xy : 
        std_dev : 
        mimo_option : 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @staticmethod
    def make(p_xy: "float", std_dev: "float", mimo_option: "int") -> "gr::ofdm::alamouti_cc::sptr":
        r"""
        make(float p_xy, float std_dev, int mimo_option) -> alamouti_cc_sptr
        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of ofdm::alamouti_cc.

        To avoid accidental use of raw pointers, ofdm::alamouti_cc's constructor is in a private implementation class. ofdm::alamouti_cc::make is the public interface for creating new instances.

        Args:
            p_xy : 
            std_dev : 
            mimo_option : 
        """
        return _ofdm_swig.alamouti_cc_make(p_xy, std_dev, mimo_option)

    def set_p_xy(self, p_xy: "float") -> "void":
        r"""set_p_xy(alamouti_cc self, float p_xy)"""
        return _ofdm_swig.alamouti_cc_set_p_xy(self, p_xy)

    def set_noise(self, std_dev: "float") -> "void":
        r"""set_noise(alamouti_cc self, float std_dev)"""
        return _ofdm_swig.alamouti_cc_set_noise(self, std_dev)

    def set_mimo_option(self, mimo_option: "int") -> "void":
        r"""set_mimo_option(alamouti_cc self, int mimo_option)"""
        return _ofdm_swig.alamouti_cc_set_mimo_option(self, mimo_option)
    __swig_destroy__ = _ofdm_swig.delete_alamouti_cc

# Register alamouti_cc in _ofdm_swig:
_ofdm_swig.alamouti_cc_swigregister(alamouti_cc)

def alamouti_cc_make(p_xy: "float", std_dev: "float", mimo_option: "int") -> "gr::ofdm::alamouti_cc::sptr":
    r"""
    alamouti_cc_make(float p_xy, float std_dev, int mimo_option) -> alamouti_cc_sptr
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of ofdm::alamouti_cc.

    To avoid accidental use of raw pointers, ofdm::alamouti_cc's constructor is in a private implementation class. ofdm::alamouti_cc::make is the public interface for creating new instances.

    Args:
        p_xy : 
        std_dev : 
        mimo_option : 
    """
    return _ofdm_swig.alamouti_cc_make(p_xy, std_dev, mimo_option)

class alamouti_cc_sptr(object):
    r"""Proxy of C++ boost::shared_ptr< gr::ofdm::alamouti_cc > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(alamouti_cc_sptr self) -> alamouti_cc_sptr
        __init__(alamouti_cc_sptr self, alamouti_cc p) -> alamouti_cc_sptr
        """
        _ofdm_swig.alamouti_cc_sptr_swiginit(self, _ofdm_swig.new_alamouti_cc_sptr(*args))

    def __deref__(self) -> "gr::ofdm::alamouti_cc *":
        r"""__deref__(alamouti_cc_sptr self) -> alamouti_cc"""
        return _ofdm_swig.alamouti_cc_sptr___deref__(self)
    __swig_destroy__ = _ofdm_swig.delete_alamouti_cc_sptr

    def make(self, p_xy: "float", std_dev: "float", mimo_option: "int") -> "gr::ofdm::alamouti_cc::sptr":
        r"""
        make(alamouti_cc_sptr self, float p_xy, float std_dev, int mimo_option) -> alamouti_cc_sptr
        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of ofdm::alamouti_cc.

        To avoid accidental use of raw pointers, ofdm::alamouti_cc's constructor is in a private implementation class. ofdm::alamouti_cc::make is the public interface for creating new instances.

        Args:
            p_xy : 
            std_dev : 
            mimo_option : 
        """
        return _ofdm_swig.alamouti_cc_sptr_make(self, p_xy, std_dev, mimo_option)

    def set_p_xy(self, p_xy: "float") -> "void":
        r"""set_p_xy(alamouti_cc_sptr self, float p_xy)"""
        return _ofdm_swig.alamouti_cc_sptr_set_p_xy(self, p_xy)

    def set_noise(self, std_dev: "float") -> "void":
        r"""set_noise(alamouti_cc_sptr self, float std_dev)"""
        return _ofdm_swig.alamouti_cc_sptr_set_noise(self, std_dev)

    def set_mimo_option(self, mimo_option: "int") -> "void":
        r"""set_mimo_option(alamouti_cc_sptr self, int mimo_option)"""
        return _ofdm_swig.alamouti_cc_sptr_set_mimo_option(self, mimo_option)

    def history(self) -> "unsigned int":
        r"""history(alamouti_cc_sptr self) -> unsigned int"""
        return _ofdm_swig.alamouti_cc_sptr_history(self)

    def declare_sample_delay(self, *args) -> "void":
        r"""
        declare_sample_delay(alamouti_cc_sptr self, int which, int delay)
        declare_sample_delay(alamouti_cc_sptr self, unsigned int delay)
        """
        return _ofdm_swig.alamouti_cc_sptr_declare_sample_delay(self, *args)

    def sample_delay(self, which: "int") -> "unsigned int":
        r"""sample_delay(alamouti_cc_sptr self, int which) -> unsigned int"""
        return _ofdm_swig.alamouti_cc_sptr_sample_delay(self, which)

    def set_output_multiple(self, multiple: "int") -> "void":
        r"""set_output_multiple(alamouti_cc_sptr self, int multiple)"""
        return _ofdm_swig.alamouti_cc_sptr_set_output_multiple(self, multiple)

    def output_multiple(self) -> "int":
        r"""output_multiple(alamouti_cc_sptr self) -> int"""
        return _ofdm_swig.alamouti_cc_sptr_output_multiple(self)

    def relative_rate(self) -> "double":
        r"""relative_rate(alamouti_cc_sptr self) -> double"""
        return _ofdm_swig.alamouti_cc_sptr_relative_rate(self)

    def relative_rate_i(self) -> "uint64_t":
        r"""relative_rate_i(alamouti_cc_sptr self) -> uint64_t"""
        return _ofdm_swig.alamouti_cc_sptr_relative_rate_i(self)

    def relative_rate_d(self) -> "uint64_t":
        r"""relative_rate_d(alamouti_cc_sptr self) -> uint64_t"""
        return _ofdm_swig.alamouti_cc_sptr_relative_rate_d(self)

    def start(self) -> "bool":
        r"""start(alamouti_cc_sptr self) -> bool"""
        return _ofdm_swig.alamouti_cc_sptr_start(self)

    def stop(self) -> "bool":
        r"""stop(alamouti_cc_sptr self) -> bool"""
        return _ofdm_swig.alamouti_cc_sptr_stop(self)

    def nitems_read(self, which_input: "unsigned int") -> "uint64_t":
        r"""nitems_read(alamouti_cc_sptr self, unsigned int which_input) -> uint64_t"""
        return _ofdm_swig.alamouti_cc_sptr_nitems_read(self, which_input)

    def nitems_written(self, which_output: "unsigned int") -> "uint64_t":
        r"""nitems_written(alamouti_cc_sptr self, unsigned int which_output) -> uint64_t"""
        return _ofdm_swig.alamouti_cc_sptr_nitems_written(self, which_output)

    def set_log_level(self, level: "std::string") -> "void":
        r"""set_log_level(alamouti_cc_sptr self, std::string level)"""
        return _ofdm_swig.alamouti_cc_sptr_set_log_level(self, level)

    def log_level(self) -> "std::string":
        r"""log_level(alamouti_cc_sptr self) -> std::string"""
        return _ofdm_swig.alamouti_cc_sptr_log_level(self)

    def max_noutput_items(self) -> "int":
        r"""max_noutput_items(alamouti_cc_sptr self) -> int"""
        return _ofdm_swig.alamouti_cc_sptr_max_noutput_items(self)

    def set_max_noutput_items(self, m: "int") -> "void":
        r"""set_max_noutput_items(alamouti_cc_sptr self, int m)"""
        return _ofdm_swig.alamouti_cc_sptr_set_max_noutput_items(self, m)

    def unset_max_noutput_items(self) -> "void":
        r"""unset_max_noutput_items(alamouti_cc_sptr self)"""
        return _ofdm_swig.alamouti_cc_sptr_unset_max_noutput_items(self)

    def is_set_max_noutput_items(self) -> "bool":
        r"""is_set_max_noutput_items(alamouti_cc_sptr self) -> bool"""
        return _ofdm_swig.alamouti_cc_sptr_is_set_max_noutput_items(self)

    def set_min_noutput_items(self, m: "int") -> "void":
        r"""set_min_noutput_items(alamouti_cc_sptr self, int m)"""
        return _ofdm_swig.alamouti_cc_sptr_set_min_noutput_items(self, m)

    def min_noutput_items(self) -> "int":
        r"""min_noutput_items(alamouti_cc_sptr self) -> int"""
        return _ofdm_swig.alamouti_cc_sptr_min_noutput_items(self)

    def max_output_buffer(self, i: "int") -> "long":
        r"""max_output_buffer(alamouti_cc_sptr self, int i) -> long"""
        return _ofdm_swig.alamouti_cc_sptr_max_output_buffer(self, i)

    def set_max_output_buffer(self, *args) -> "void":
        r"""
        set_max_output_buffer(alamouti_cc_sptr self, long max_output_buffer)
        set_max_output_buffer(alamouti_cc_sptr self, int port, long max_output_buffer)
        """
        return _ofdm_swig.alamouti_cc_sptr_set_max_output_buffer(self, *args)

    def min_output_buffer(self, i: "int") -> "long":
        r"""min_output_buffer(alamouti_cc_sptr self, int i) -> long"""
        return _ofdm_swig.alamouti_cc_sptr_min_output_buffer(self, i)

    def set_min_output_buffer(self, *args) -> "void":
        r"""
        set_min_output_buffer(alamouti_cc_sptr self, long min_output_buffer)
        set_min_output_buffer(alamouti_cc_sptr self, int port, long min_output_buffer)
        """
        return _ofdm_swig.alamouti_cc_sptr_set_min_output_buffer(self, *args)

    def pc_noutput_items(self) -> "float":
        r"""pc_noutput_items(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_noutput_items(self)

    def pc_noutput_items_avg(self) -> "float":
        r"""pc_noutput_items_avg(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_noutput_items_avg(self)

    def pc_noutput_items_var(self) -> "float":
        r"""pc_noutput_items_var(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_noutput_items_var(self)

    def pc_nproduced(self) -> "float":
        r"""pc_nproduced(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_nproduced(self)

    def pc_nproduced_avg(self) -> "float":
        r"""pc_nproduced_avg(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_nproduced_avg(self)

    def pc_nproduced_var(self) -> "float":
        r"""pc_nproduced_var(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_nproduced_var(self)

    def pc_input_buffers_full(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_input_buffers_full(alamouti_cc_sptr self, int which) -> float
        pc_input_buffers_full(alamouti_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.alamouti_cc_sptr_pc_input_buffers_full(self, *args)

    def pc_input_buffers_full_avg(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_input_buffers_full_avg(alamouti_cc_sptr self, int which) -> float
        pc_input_buffers_full_avg(alamouti_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.alamouti_cc_sptr_pc_input_buffers_full_avg(self, *args)

    def pc_input_buffers_full_var(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_input_buffers_full_var(alamouti_cc_sptr self, int which) -> float
        pc_input_buffers_full_var(alamouti_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.alamouti_cc_sptr_pc_input_buffers_full_var(self, *args)

    def pc_output_buffers_full(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_output_buffers_full(alamouti_cc_sptr self, int which) -> float
        pc_output_buffers_full(alamouti_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.alamouti_cc_sptr_pc_output_buffers_full(self, *args)

    def pc_output_buffers_full_avg(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_output_buffers_full_avg(alamouti_cc_sptr self, int which) -> float
        pc_output_buffers_full_avg(alamouti_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.alamouti_cc_sptr_pc_output_buffers_full_avg(self, *args)

    def pc_output_buffers_full_var(self, *args) -> "std::vector< float,std::allocator< float > >":
        r"""
        pc_output_buffers_full_var(alamouti_cc_sptr self, int which) -> float
        pc_output_buffers_full_var(alamouti_cc_sptr self) -> pmt_vector_float
        """
        return _ofdm_swig.alamouti_cc_sptr_pc_output_buffers_full_var(self, *args)

    def pc_work_time(self) -> "float":
        r"""pc_work_time(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_work_time(self)

    def pc_work_time_avg(self) -> "float":
        r"""pc_work_time_avg(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_work_time_avg(self)

    def pc_work_time_var(self) -> "float":
        r"""pc_work_time_var(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_work_time_var(self)

    def pc_work_time_total(self) -> "float":
        r"""pc_work_time_total(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_work_time_total(self)

    def pc_throughput_avg(self) -> "float":
        r"""pc_throughput_avg(alamouti_cc_sptr self) -> float"""
        return _ofdm_swig.alamouti_cc_sptr_pc_throughput_avg(self)

    def set_processor_affinity(self, mask: "std::vector< int,std::allocator< int > > const &") -> "void":
        r"""set_processor_affinity(alamouti_cc_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _ofdm_swig.alamouti_cc_sptr_set_processor_affinity(self, mask)

    def unset_processor_affinity(self) -> "void":
        r"""unset_processor_affinity(alamouti_cc_sptr self)"""
        return _ofdm_swig.alamouti_cc_sptr_unset_processor_affinity(self)

    def processor_affinity(self) -> "std::vector< int,std::allocator< int > >":
        r"""processor_affinity(alamouti_cc_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _ofdm_swig.alamouti_cc_sptr_processor_affinity(self)

    def active_thread_priority(self) -> "int":
        r"""active_thread_priority(alamouti_cc_sptr self) -> int"""
        return _ofdm_swig.alamouti_cc_sptr_active_thread_priority(self)

    def thread_priority(self) -> "int":
        r"""thread_priority(alamouti_cc_sptr self) -> int"""
        return _ofdm_swig.alamouti_cc_sptr_thread_priority(self)

    def set_thread_priority(self, priority: "int") -> "int":
        r"""set_thread_priority(alamouti_cc_sptr self, int priority) -> int"""
        return _ofdm_swig.alamouti_cc_sptr_set_thread_priority(self, priority)

    def name(self) -> "std::string":
        r"""name(alamouti_cc_sptr self) -> std::string"""
        return _ofdm_swig.alamouti_cc_sptr_name(self)

    def symbol_name(self) -> "std::string":
        r"""symbol_name(alamouti_cc_sptr self) -> std::string"""
        return _ofdm_swig.alamouti_cc_sptr_symbol_name(self)

    def input_signature(self) -> "gr::io_signature::sptr":
        r"""input_signature(alamouti_cc_sptr self) -> io_signature_sptr"""
        return _ofdm_swig.alamouti_cc_sptr_input_signature(self)

    def output_signature(self) -> "gr::io_signature::sptr":
        r"""output_signature(alamouti_cc_sptr self) -> io_signature_sptr"""
        return _ofdm_swig.alamouti_cc_sptr_output_signature(self)

    def unique_id(self) -> "long":
        r"""unique_id(alamouti_cc_sptr self) -> long"""
        return _ofdm_swig.alamouti_cc_sptr_unique_id(self)

    def to_basic_block(self) -> "gr::basic_block_sptr":
        r"""to_basic_block(alamouti_cc_sptr self) -> basic_block_sptr"""
        return _ofdm_swig.alamouti_cc_sptr_to_basic_block(self)

    def check_topology(self, ninputs: "int", noutputs: "int") -> "bool":
        r"""check_topology(alamouti_cc_sptr self, int ninputs, int noutputs) -> bool"""
        return _ofdm_swig.alamouti_cc_sptr_check_topology(self, ninputs, noutputs)

    def alias(self) -> "std::string":
        r"""alias(alamouti_cc_sptr self) -> std::string"""
        return _ofdm_swig.alamouti_cc_sptr_alias(self)

    def set_block_alias(self, name: "std::string") -> "void":
        r"""set_block_alias(alamouti_cc_sptr self, std::string name)"""
        return _ofdm_swig.alamouti_cc_sptr_set_block_alias(self, name)

    def _post(self, which_port: "swig_pmt_ptr", msg: "swig_pmt_ptr") -> "void":
        r"""_post(alamouti_cc_sptr self, swig_pmt_ptr which_port, swig_pmt_ptr msg)"""
        return _ofdm_swig.alamouti_cc_sptr__post(self, which_port, msg)

    def message_ports_in(self) -> "pmt::pmt_t":
        r"""message_ports_in(alamouti_cc_sptr self) -> swig_pmt_ptr"""
        return _ofdm_swig.alamouti_cc_sptr_message_ports_in(self)

    def message_ports_out(self) -> "pmt::pmt_t":
        r"""message_ports_out(alamouti_cc_sptr self) -> swig_pmt_ptr"""
        return _ofdm_swig.alamouti_cc_sptr_message_ports_out(self)

    def message_subscribers(self, which_port: "swig_pmt_ptr") -> "pmt::pmt_t":
        r"""message_subscribers(alamouti_cc_sptr self, swig_pmt_ptr which_port) -> swig_pmt_ptr"""
        return _ofdm_swig.alamouti_cc_sptr_message_subscribers(self, which_port)

# Register alamouti_cc_sptr in _ofdm_swig:
_ofdm_swig.alamouti_cc_sptr_swigregister(alamouti_cc_sptr)


alamouti_cc_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
alamouti_cc = alamouti_cc.make;


