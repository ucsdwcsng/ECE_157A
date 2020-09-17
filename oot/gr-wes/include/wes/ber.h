/* -*- c++ -*- */
/*
 * Copyright 2020 pling.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_WES_BER_H
#define INCLUDED_WES_BER_H

#include <wes/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace wes {

    /*!
     * \brief <+description of block+>
     * \ingroup wes
     *
     */
    class WES_API ber : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<ber> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of wes::ber.
       *
       * To avoid accidental use of raw pointers, wes::ber's
       * constructor is in a private implementation
       * class. wes::ber::make is the public interface for
       * creating new instances.
       */
      static sptr make(int bits_per_byte, int reset_ber);

      virtual void reset_stats(int reset_ber) = 0;
    };

  } // namespace wes
} // namespace gr

#endif /* INCLUDED_WES_BER_H */
